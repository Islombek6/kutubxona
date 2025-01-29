from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Student, KUtubxonachi, Record, Kitob, Muallif


def home_view(request):
    today = datetime.today()
    context = {
        'today': today,
    }
    return render(request, 'home.html', context)


# ---------------------------------------------------------------------------------------------------#
#                   """T"""      /\     |          /\     |""""\      /\                             #
#                      |        /  \    |         /  \    |  ° /     /  \                            #
#                      |       /""""\   |        /""""\   |  0  \   /""""\                           #
#                      |      /      \  |_____  /      \  |_____/  /      \                          #
# ---------------------------------------------------------------------------------------------------#

def talabalar_view(request):
    talabalar = Student.objects.all()
    guruhlar = [item['gurux'] for item in Student.objects.all().values('gurux')]
    guruhlar = sorted(list(set(guruhlar)))

    search = request.GET.get('search')
    kurs = request.GET.get('kurs')
    gurux = request.GET.get('gurux')

    if search is not None:
        talabalar = talabalar.filter(ism__icontains=search)
    if kurs is not None and kurs != '0':
        talabalar = talabalar.filter(kurs=kurs)
    if gurux is not None and gurux != '0':
        talabalar = talabalar.filter(gurux=gurux)

    context = {
        'talabalar': talabalar,
        'guruhlar': guruhlar,
        'kurs': kurs,
        'search': search,
        'gurux': gurux,
    }
    return render(request, 'talabalar.html', context)


def talaba_qoshish_view(request):
    if request.method == 'POST':
        Student.objects.create(
            ism=request.POST.get('ism'),
            gurux=request.POST.get('gurux'),
            kurs=request.POST.get('kurs'),
            kitoblar_soni=request.POST.get('kitoblar_soni'),
        )
        return redirect('talabalar')
    return render(request, 'talaba_qoshish.html')


def talaba_update_view(request, pk):
    talaba = get_object_or_404(Student, id=pk)
    if request.method == 'POST':
        talaba.ism = request.POST.get('ism')
        talaba.gurux = request.POST.get('gurux')
        talaba.kurs = request.POST.get('kurs')
        talaba.kitoblar_soni = request.POST.get('kitoblar_soni')
        talaba.save()
        return redirect('talabalar')
    context = {
        'talaba': talaba,
    }
    return render(request, 'talaba_update.html', context)


def talaba_delete_confirm_view(request, talaba_id):
    talaba = Student.objects.get(id=talaba_id)
    context = {
        'talaba': talaba
    }
    return render(request, 'talaba_delete_confirm.html', context)


def talaba_delete_view(request, talaba_id):  # noqa
    talabalar = Student.objects.get(id=talaba_id)
    talabalar.delete()
    return redirect('talabalar')


def talabalar_details_view(request, talaba_id):
    talaba = Student.objects.get(id=talaba_id)
    context = {
        'talaba': talaba,
    }
    return render(request, 'talaba_details.html', context)


# ---------------------------------------------------------------------------------------------------#
#                |\    /|    |     |      /\     |        |       "T"   |"""""                       #
#                | \  / |    |     |     /  \    |        |        |    |                            #
#                |  \/  |    |     |    /""""\   |        |        |    |"""                         #
#                |      |     \____|   /      \  |_____   |_____  _|_   |                            #
# ---------------------------------------------------------------------------------------------------#

def mualliflar_view(request):
    mualliflar = Muallif.objects.all()
    search = request.GET.get('search')
    if search is not None:
        mualliflar = mualliflar.filter(ism__icontains=search)
    context = {
        'mualliflar': mualliflar,
    }
    return render(request, 'mualliflar.html', context)


def muallif_qoshish_view(request):
    if request.method == 'POST':
        Muallif.objects.create(
            ism=request.POST.get('ism'),
            jins=request.POST.get('ism'),
            t_sana=request.POST.get('t_sana'),
            kitob_soni=request.POST.get('kitob_soni'),
            tirik=request.POST.get('tirik') == 'on',
        )
        return redirect('mualliflar')
    return render(request, 'muallif_qoshish.html')


def muallif_update_view(request, pk):
    muallif = get_object_or_404(Muallif, id=pk)
    if request.method == 'POST':
        Muallif.objects.filter(id=pk).update(
            ism=request.POST.get('ism'),
            jins=request.POST.get('jins'),
            t_sana=request.POST.get('t_sana'),
            kitob_soni=request.POST.get('kitob_soni'),
            tirik=request.POST.get('tirik') == 'on',
        )
        return redirect('mualliflar')
    context = {
        'muallif': muallif,
    }
    return render(request, 'muallif_update.html', context)


def muallif_delete_confrim_view(request, pk):
    muallif = Muallif.objects.get(id=pk)
    context = {
        'muallif': muallif,
    }
    return render(request, 'muallif_delete_confrim.html', context)


def muallif_delete(request, muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    muallif.delete()
    return redirect('mualliflar')


def mualliflar_details_view(request, muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    context = {
        'muallif': muallif,
    }
    return render(request, 'muallif_details.html', context)


# ---------------------------------------------------------------------------------------------------#
#                              |  /  "T"  """T"""  /"""\   |""""\                                    #
#                              | /    |      |    |  ∩  |  |  ° /                                    #
#                              | \    |      |    |  U  |  |  0  \                                   #
#                              |  \  _|_     |     \___/   |_____/                                   #
# ---------------------------------------------------------------------------------------------------#

def kitob_view(request):
    kitoblar = Kitob.objects.all()
    mualliflar = [Muallif.objects.get(id=id) for id in set(Kitob.objects.all().values_list('muallif', flat=True))]

    muallif = request.GET.get('muallif')
    search = request.GET.get('search')
    if search is not None:
        kitoblar = kitoblar.filter(nom__icontains=search)

    if muallif is not None and muallif != '0':
        kitoblar = kitoblar.filter(muallif__id=muallif)

    context = {
        'kitoblar': kitoblar,
        'mualliflar': mualliflar,
        'search': search,
    }
    return render(request, 'kitoblar.html', context)


def kitob_qoshish_view(request):
    if request.method == 'POST':
        Kitob.objects.create(
            nom=request.POST.get('nom'),
            Janr=request.POST.get('Janr'),
            sahifa=request.POST.get('sahifa'),
            muallif=Muallif.objects.get(id=request.POST.get('muallif_id')),

        )
        return redirect("kitoblar")
    context = {
        'mualliflar': Muallif.objects.all(),

    }
    return render(request, 'kitob_qoshish.html', context)


def kitob_delete_confrim_view(request, pk):
    kitob = Kitob.objects.get(id=pk)
    context = {
        'kitob': kitob,
    }
    return render(request, 'kitob_delete_confrim.html', context)


def kitob_update_view(request, pk):
    kitob = get_object_or_404(Kitob, id=pk)
    if request.method == 'POST':
        Kitob.objects.filter(id=pk).update(
            nom=request.POST.get('nom'),
            Janr=request.POST.get('Janr'),
            sahifa=request.POST.get('sahifa'),
            muallif=get_object_or_404(Muallif, id=request.POST.get('muallif_id'))
        )
        return redirect('kitoblar')
    mualliflar = Muallif.objects.all()
    context = {
        'kitob': kitob,
        'mualliflar': mualliflar
    }
    return render(request, 'kitob_update.html', context)


def kitob_delete(request, kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    kitob.delete()
    return redirect('kitoblar')


def kitoblar_details_view(request, kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    context = {
        'kitob': kitob,
    }
    return render(request, 'kitob_details.html', context)


# ---------------------------------------------------------------------------------------------------------------#
#        |  / |     |   """T""" |     |   |""""\    \  /    /"""\   |\   |     /\      /""""\  |    |    "T"     #
#        | /  |     |      |    |     |   |  ° /     \/    |  ∩  |  | \  |    /  \    |        |____|     |      #
#        | \  |     |      |    |     |   |  0  \    /\    |  U  |  |  \ |   /""""\   |        |    |     |      #
#        |  \  \____|      |     \____|   |_____/   /  \    \___/   |   \|  /      \   \____/  |    |    _|_     #
# ---------------------------------------------------------------------------------------------------------------#

def kutubxonachi_view(request):
    kutubxonachilar = KUtubxonachi.objects.all()
    search = request.GET.get('search')

    if search is not None:
        kutubxonachilar = kutubxonachilar.filter(ism__icontains=search)
    context = {
        'kutubxonachilar': kutubxonachilar,
    }
    return render(request, 'kutubxonachilar.html', context)


def kutubxonachi_details_view(request, kutubxonachi_id):
    kutubxonachi = KUtubxonachi.objects.get(id=kutubxonachi_id)
    context = {
        'kutubxonachi': kutubxonachi,
    }
    return render(request, 'kutubxonachi_details.html', context)


def kutubxonachi_qoshish_view(request):
    if request.method == 'POST':
        KUtubxonachi.objects.create(
            ism=request.POST.get('ism'),
            ish_vaqt=request.POST.get('ish_vaqt')
        )
        return redirect("kutubxonachilar")

    return render(request, 'kutubxonachi_qoshish.html', )


def kutubxonachi_update_view(request, pk):
    kutubxonachi = get_object_or_404(KUtubxonachi, id=pk)
    if request.method == 'POST':
        kutubxonachi.ism = request.POST.get('ism')
        kutubxonachi.ish_vaqt = request.POST.get('ish_vaqt')
        kutubxonachi.save()
        return redirect('kutubxonachilar')
    context = {
        'kutubxonachi': kutubxonachi,
    }
    return render(request, 'kutubxonachi_update.html', context)


def kutubxonachi_delete_confirm_view(request, pk):
    kutubxonachi = KUtubxonachi.objects.get(id=pk)
    context = {
        'kutubxonachi': kutubxonachi,
    }
    return render(request, 'kutubxonachi_delete_confirm.html', context)


def kutubxonachi_delete_view(request, kutubxonachi_id):
    kutubxonachi = KUtubxonachi.objects.get(id=kutubxonachi_id)
    kutubxonachi.delete()
    return redirect('kutubxonachilar')


# ---------------------------------------------------------------------------------------------------#
#             |"""\    |""""  |  /  /"""\ 9  |"""\   |""""\    |          /\      |"""\              #
#             | 0 /    |____  | /  |  ∩  |   | 0 /   |     |   |         /  \     | 0 /              #
#             |   \    |      | \  |  U  |   |   \   |     |   |        /""""\    |   \              #
#             |    \   |____  |  \  \___/    |    \  |____/    |_____  /      \   |    \             #
# ---------------------------------------------------------------------------------------------------#

def recordlar_view(request):
    recordlar = Record.objects.all()
    search = request.GET.get('search')

    if search is not None:
        recordlar = recordlar.filter(student__ism__icontains=search)

    context = {
        'recordlar': recordlar,
    }
    return render(request, 'recordlar.html', context)


def record_update_view(request, pk):
    record = get_object_or_404(Record, id=pk)
    if request.method == "POST":
        qaytardi = request.POST.get('qaytardi')
        if qaytardi == "on":
            qaytardi = True
        else:
            qaytardi = False
        Record.objects.filter(id=pk).update(
            student=get_object_or_404(Student, id=request.POST.get('student_id')),
            kitob=get_object_or_404(Kitob, id=request.POST.get('kitob_id')),
            kutubxonachi=get_object_or_404(KUtubxonachi, id=request.POST.get('kutubxonachi_id')),
            olingan_sana=request.POST.get('olingan_sana'),
            qaytardi=qaytardi,
        )
        qaytargan_sana = request.POST.get('qaytargan_sana', None)
        if qaytargan_sana is not None:
            Record.objects.filter(id=pk).update(
                qaytargan_sana=qaytargan_sana,
            )
            return redirect('recordlar')
    studentlar = Student.objects.all()
    kitoblar = Kitob.objects.all()
    kutubxonachilar = KUtubxonachi.objects.all()
    context = {
        'record': record,
        'studentlar': studentlar,
        "kitoblar": kitoblar,
        "kutubxonachilar": kutubxonachilar,
    }
    return render(request, 'record_update.html', context)


def record_delete_confrim_view(request, pk):
    record = Record.objects.get(id=pk)
    context = {
        'record': record,
    }
    return render(request, 'record_delete_confrim.html', context)


def record_delete(request, record_id):
    record = Record.objects.get(id=record_id)
    record.delete()
    return redirect('recordlar')


def recordlar_details_view(request, record_id):
    record = Record.objects.get(id=record_id)
    context = {
        'record': record,
    }
    return render(request, 'record_details.html', context)


def record_qoshish_view(request):
    if request.method == 'POST':
        Record.objects.create(
            student=Student.objects.get(id=request.POST.get('talaba_id')),
            kitob=Kitob.objects.get(id=request.POST.get('kitob_id')),
            kutubxonachi=KUtubxonachi.objects.get(id=request.POST.get('kutubxonachi_id')),
            olingan_sana=request.POST.get('olingan_sana'),
            qaytargan_sana=request.POST.get('qaytarilgan_sana'),
            qaytardi=request.POST.get('qaytardi') == 'on', )
        return redirect('recordlar')
    context = {
        'talabalar': Student.objects.all(),
        'kitoblar': Kitob.objects.all(),
        'kutubxonachilar': KUtubxonachi.objects.all(),
    }
    return render(request, 'record_qoshish.html', context)
