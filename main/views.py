from django import forms
from django.contrib import messages
from django.db import transaction
from django.shortcuts import render
from django.views import View

from main.models import UpgradeRequest, Contract


class UpgradeRequestForm(forms.ModelForm):
    action = forms.CharField()

    class Meta:
        model = UpgradeRequest
        fields = ['note_by_approver']


class Index(View):
    def get(self, req):
        return render(req, 'requests.html', context={'requests': UpgradeRequest.objects.filter(status='N')})


class RequestApproval(View):

    def get(self, request, req_id):
        req = UpgradeRequest.objects.get(pk=req_id)
        form = UpgradeRequestForm(instance=req)
        return render(request, 'approval.html', context={'form': form, 'req': req})

    @transaction.atomic
    def post(self, request, req_id):
        upgrade_request = UpgradeRequest.objects.get(pk=req_id)
        form = UpgradeRequestForm(request.POST, instance=upgrade_request)
        if form.is_valid():
            form.save()
            if form.cleaned_data['action'] == 'Approve':
                self._approve(request, req_id)
            else:
                self._reject(request, upgrade_request)
        else:
            messages.error(request, 'Invalid input')

        return render(request, 'approval.html', context={'form': form, 'req': upgrade_request})

    def _reject(self, request, upgrade_request):
        raise NotImplementedError()

    def _approve(self, request, upgrade_request_id):
        upgrade_request = UpgradeRequest.objects.get(pk=upgrade_request_id)

        # First, do some checks to not end up in inconsistent state
        blocker_reason = upgrade_request.approval_blocked_by
        if blocker_reason is not None:
            messages.error(request, blocker_reason)
            return

        # OK, everything is fine, let's do the work.
        upgrade_request.status = 'A'
        Contract.objects.create(
            customer=upgrade_request.customer,
            text='We agree that we will be nice to each other.\n\nSigned ...... and ......'
        )
        upgrade_request.customer.status = 'P'
        upgrade_request.customer.save()
        upgrade_request.save()
