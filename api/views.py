from django.shortcuts import render
from .algorithms import simple_search, linear_search

ALGORITHMS_MAP = {
    'simple': simple_search,
    'linear_search': linear_search,
}


def main(request):
    errors = validate(request)
    if errors:
        return render(request, 'main.html', {'success': False, 'errors': errors})

    if not request.POST.get('codon'):
        return render(request, 'main.html')

    search_alg = ALGORITHMS_MAP[request.POST.get('search_alg')]

    if not search_alg(request.POST.get('codon')):
        return render(request, 'main.html', {'success': False, 'errors': ['The codon was not found in the chain.']})
    else:
        return render(request, 'main.html', {'success': True, 'message': 'The codon was found in the chain.'})


def validate(request):
    errors = []
    if request.POST.get('search_alg'):
        if not request.POST.get('search_alg') in ALGORITHMS_MAP:
            errors.append('incorrect algorithm passed')
    if request.POST.get('codon'):
        gens = ['a', 'c', 'g', 't']
        codon_char_arr = list(request.POST.get('codon'))
        result = list(set(codon_char_arr) - set(gens))
        if len(result):
            errors.append('codon has incorrect genes')
        return errors
