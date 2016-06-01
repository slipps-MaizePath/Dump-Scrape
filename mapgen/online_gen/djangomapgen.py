from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from applets import field_map_generator


@login_required
def download_field_map(request):
  plot_loader = sort_plot_loader(request)
  plot_objects = []  # Init: (range, row, experiment, plot_id)
  for obs in plot_loader:
    row_num = obs.obs_plot.row_num
    range_num = field_map_generator._get_column_letter(int(obs.obs_plot.range_num))

    plot_objects.append(field_map_generator.PlotCell(
       range_num=range_num, row_num=row_num, experiment=obs.experiment, plot_id=obs.obs_plot.plot_id, field=obs.experiment.field)
    )

  wb = field_map_generator.compile_info(plot_objects)
  response = HttpResponse(save_virtual_workbook(wb), content_type='application/vnd.ms-excel')
  response['Content-Disposition'] = 'attachment; filename="selected_experiment_maps.xlsx"'

  return response
