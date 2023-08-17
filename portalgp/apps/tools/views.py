from django.shortcuts import render, redirect
from django.contrib import messages

from apps.game.gps.models import GP
from apps.game.mbds.models import MBD
from apps.game.drgs.models import DRG

from .forms import LinkFkForm, CalculateGPPositionsForm, CalculateGPStreaksForm

def tools(request):
    return render(request, 'tools/tools.html', {})

def link_fk(request):
    form = LinkFkForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                warnings = []
                start_date = form.cleaned_data['start_date']
                end_date = form.cleaned_data['end_date']
                ignore_locked = form.cleaned_data['ignore_locked']
                update_gp = form.cleaned_data['update_gp']
                update_mbd_and_drg = form.cleaned_data['update_mbd_and_drg']

                if update_gp:
                    if ignore_locked:
                        gps_in_range = GP.objects.filter(date__range=(start_date, end_date))
                    else:
                        gps_in_range = GP.objects.filter(date__range=(start_date, end_date), locked=False)

                    for gp in gps_in_range:
                        day_mbd_queryset = MBD.objects.filter(date=gp.date)
                        if len(day_mbd_queryset) == 1:
                            gp.mbd = day_mbd_queryset[0]
                        if len(day_mbd_queryset) == 0:
                            # no hay M.B.D.
                            warnings.append(f"G.P. ID {gp.id} no tiene ningún M.B.D. en ese mismo día.")
                        if len(day_mbd_queryset) > 1:
                            # hay más de un MBD por día...
                            warnings.append(f"G.P. ID {gp.id} tiene más de un M.B.D. en el mismo día ({gp.date}) y no se le ha asignado ninguno.")
                        gp.save()

                if update_mbd_and_drg:
                    mbds_in_range = MBD.objects.filter(date__range=(start_date, end_date), locked=False)
                    drgs_in_range = DRG.objects.filter(date__range=(start_date, end_date), locked=False)

                    # Actualizar MBDs
                    for mbd in mbds_in_range:
                        day_drg_queryset = DRG.objects.filter(date=mbd.date)
                        if len(day_drg_queryset) == 1:
                            mbd.drg = day_drg_queryset[0]
                        if len(day_drg_queryset) == 0:
                            pass
                        else:
                            # hay más de un DRG por día...
                            pass
                        mbd.save()

                    # Actualizar Drgs. Esto se podría unir en el loop de los mbd?
                    for drg in drgs_in_range:
                        day_mbd_queryset = MBD.objects.filter(date=drg.date)
                        if len(day_mbd_queryset) == 1:
                            drg.mbd = day_mbd_queryset[0]
                        else:
                            # hay más de un MBD por día...
                            pass
                        drg.save()

                if warnings:
                    messages.warning(request, '\n'.join(warnings))
                    
                messages.success(request, "Se han actualizado los ID.")
                return redirect('link_fk')
        return render(request, 'tools/link_fk.html', {'form':form})
    else:
        messages.error(request, "Debes iniciar sesión")
        return redirect("home")
    
def calculate_gp_positions_render(request):
    form = CalculateGPPositionsForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                start_date = form.cleaned_data['start_date']
                end_date = form.cleaned_data['end_date']
                ignore_locked = form.cleaned_data['ignore_locked']

                calculate_gp_positions(use_range=True, start_date=start_date, end_date=end_date, ignore_locked=ignore_locked)

                messages.success(request, "Se han actualizado las posiciones de los G.P.")
                return redirect('calculate_gp_positions')
        return render(request, 'tools/calculate_gp_positions.html', {'form':form})
    else:
        messages.error(request, "Debes iniciar sesión")
        return redirect("tools")
    

def calculate_gp_positions(request, start_date, end_date, ignore_locked=True, use_range=True):
    if request.user.is_authenticated:
        warnings = []
        gps_in_range = GP.objects.filter(date__range=(start_date, end_date))
        unique_dates = gps_in_range.dates('date', 'day')

        for date in unique_dates:
            objects_for_date = GP.objects.filter(date=date, valid='Si').order_by('time')

            position = 1

            for obj in objects_for_date:
                obj.position = position

                if ignore_locked:
                    if obj.locked == True:
                        obj.save()
                else:
                    if obj.locked == True:
                        pass
                    else:
                        obj.save()

                position += 1

            not_valid_objects = GP.objects.filter(date=date, valid='No').order_by('time')
            for not_valid_gp in not_valid_objects:
                not_valid_gp.position = None
                not_valid_gp.save()

        if warnings:
            messages.warning(request, '\n'.join(warnings))
            
        messages.success(request, "Se han actualizado las posiciones de los G.P.")
        return redirect('calculate_gp_positions')
    else:
        messages.error(request, "Debes iniciar sesión")
        return redirect("tools")

def calculate_gp_streaks(request):
    pass