from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UploadFileForm
from django.contrib.sessions.models import Session
from django.db.utils import IntegrityError

from apps.game.gps.models import GP
from apps.game.mbds.models import MBD
from apps.game.drgs.models import DRG
from apps.persons.models import Person

from datetime import datetime

from .scripts.read_wtext import WText
from .scripts.get_player_id import get_player_id

def wimport(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                file_content = file.read().decode('utf-8')
                wtext = WText(text=file_content, use_range=False)
                request.session['wtext_gps'] = wtext.get_gps()
                request.session['wtext_mbds'] = wtext.get_mbds()
                request.session['wtext_drgs'] = wtext.get_drgs()
            except:
                messages.error(request, "El archivo que has subido no es válido. Asegúrate de que es un .txt exportado directamente de WhatsApp.")
                return redirect('wimport')

            return render(request, 'wimport/preview.html', {'wtext': wtext})
    else:
        form = UploadFileForm()
        return render(request, 'wimport/import.html', {'form': form})
    
def upload_wtext_to_db(request):
    if request.user.is_authenticated:
        wtext_gps = request.session.get('wtext_gps', None)
        wtext_mbds = request.session.get('wtext_mbds', None)
        wtext_drgs = request.session.get('wtext_drgs', None)

        gp_amount = len(wtext_gps)
        mbd_amount = len(wtext_mbds)
        drg_amount = len(wtext_drgs)

        for gp_item in wtext_gps:
            try:
                GP.objects.create(
                    date = datetime.strptime(gp_item[0], "%d/%m/%y").date(),
                    time = datetime.strptime(gp_item[1], "%H:%M").time(),
                    person = Person.objects.get(id=get_player_id(gp_item[2])),
                    message = gp_item[3]
                )
            except IntegrityError as e:
                messages.error(request, "Error: " + str(e))

        for mbd_item in wtext_mbds:
            try:
                MBD.objects.create(
                    date = datetime.strptime(mbd_item[0], "%d/%m/%y").date(),
                    time = datetime.strptime(mbd_item[1], "%H:%M").time(),
                    person = Person.objects.get(id=get_player_id(mbd_item[2])),
                    message = mbd_item[3]
                )
            except IntegrityError as e:
                messages.error(request, "Error: " + str(e))

        for drg_item in wtext_drgs:
            try:
                DRG.objects.create(
                    date = datetime.strptime(drg_item[0], "%d/%m/%y").date(),
                    time = datetime.strptime(drg_item[1], "%H:%M").time(),
                    person = Person.objects.get(id=get_player_id(drg_item[2])),
                    message = drg_item[3]
                )
            except IntegrityError as e:
                messages.error(request, "Error: " + str(e))    

        messages.success(request, 'Los datos se han subido a la base de datos con éxito.')
        return render(request, 'wimport/upload_wtext_to_db.html', {'gps': wtext_gps, 'mbds': wtext_mbds, 'drgs': wtext_drgs, 'gp_amount': gp_amount, 'mbd_amount': mbd_amount, 'drg_amount': drg_amount})
    else:
        messages.error(request, 'Debes iniciar sesión')
        return redirect('wimport')