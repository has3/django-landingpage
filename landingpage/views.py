# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from landingpage.forms import SignUpForm, EmailForm
from landingpage.models import LandingPage


# def thank_you(request):
#     """
#      Basic email sending view assumes we redirect to thank you page
#     """
#     if request.POST:
#         form = EmailForm(request.POST)
#         if form.is_valid():
#             send_mail('subject','our content', 'porfirio84@gmail.com', form.cleaned_data['emails'].split(','))
#
#     return render_to_response('landingpage/thankyou.html', context_instance=RequestContext(request))

class NewCreateView(CreateView):
    form_class = SignUpForm

    def form_valid(self, form):
        email = self.request.POST['email']
        organization = self.request.POST['organization']
        send_mail('subject', "Email: {0} \n Organization: {1}".format(email, organization), 'anthony@gmail.com', ['anthonybui@gmail.com'], fail_silently=True)
        return super(NewCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(NewCreateView, self).get_context_data(**kwargs)
        landing_page_obj = LandingPage.objects.select_related().get(id=1)
        context.update({'landing_page': landing_page_obj})
        return context