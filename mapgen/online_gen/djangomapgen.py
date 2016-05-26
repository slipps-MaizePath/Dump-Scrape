from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from applets import field_map_generator

@login_required
def download_field_map(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="selected_experiment_maps.csv"'
    plot_loader = sort_plot_loader(request)
    plot_dict = {}
    rows = []
    ranges = []
    experiments = []
    for obs in plot_loader:
        plot_id = obs.obs_plot.plot_id
        row_num = obs.obs_plot.row_num
        range_num = field_map_generator.number_to_letter(obs.obs_plot.range_num)
        exp = obs.experiment.name + ': ' + obs.experiment.start_date

        coords = range_num + str(row_num)
        plot_dict[coords] = plot_id
        rows.append(int(row_num))
        ranges.append(range_num)
        experiments.append(exp)

    domain = [rows, ranges]
    info = (plot_dict, domain, set(experiments))

    response = field_map_generator.compile_info(info, response)

    return response
