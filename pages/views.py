from django.shortcuts import render


def main(req):
    return render(req, 'pages/index.html')


def portfolio(req, n=None):
    context = {'n': n}
    return render(req, 'pages/portfolio.html', context=context)

