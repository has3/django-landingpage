from landingpage.utils import setting

def cta(request):
    twitter_cta = setting('TWITTER_CTA', "Please check out Elevate, it let's your work speak for itself")
    share_cta = setting('SHARE_CTA', 'Thanks! We will be contacting you shortly. Until then please help us spread the word by sharing with your network.')
    return {'twitter_cta': twitter_cta,
            'share_cta': share_cta}

