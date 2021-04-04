from rest_framework.views import APIView
from rest_framework.response import Response
import random
from app import models


# class DashBoardView(View):
#
#     def get(self, request):
#         counts = {
#             'asset': models.Asset.objects.all().count(),
#             'server': models.Asset.objects.filter(category__name='服務器').count(),
#             'netware': models.Asset.objects.filter(category__name='網路設備').count(),
#             'host': models.Asset.objects.filter(category__name='虛擬機').count(),
#
#         }
#
#         return render(request, 'dashboard.html', locals())


class DashRackView(APIView):

    def get(self, request):
        busline_obj = models.Busline.objects.all()

        data = {'label': [], 'data': []}
        for busline in busline_obj:
            data['data'].append(models.Asset.objects.filter(busline=busline).count())
            data['label'].append(busline.name)

        return Response(data)


class DashAssetView(APIView):

    def recent_seven_days(self):
        import datetime
        from django.utils import timezone
        today = timezone.now().date()
        # lists = []
        for i in range(7):
            # lists.append(date.strftime('%Y-%m-%d'))
            yield today - datetime.timedelta(days=i)

    def get(self, request):
        # print('recent_seven_days', self.recent_seven_days())
        random_range_num = list(range(20))
        list_week_day = list(self.recent_seven_days())
        list_week_day.reverse()

        server_list = []
        netware_list = []
        vm_list = []

        for day in list_week_day:
            server_list.append(random.choice(random_range_num))
            netware_list.append(random.choice(random_range_num))
            vm_list.append(random.choice(random_range_num))

        data = {
            'label': [i.strftime('%Y-%m-%d') for i in list_week_day],
            'server_list': server_list,
            'netware_list': netware_list,
            'vm_list': vm_list,
        }

        return Response(data)


class DashBoardView(APIView):
    # permission_classes = (permissions.AllowAny,)

    def recent_seven_days(self):
        import datetime
        from django.utils import timezone
        today = timezone.now().date()
        for i in range(7):
            yield today - datetime.timedelta(days=i)

    def get_count(self):

        counts = [
            {'title': '服務器', 'icon': 'asterisk',
             'count': models.Category.objects.get(name='服務器').asset_set.all().count(), 'color': '#2d8cf0'},
            {'title': '虛擬機', 'icon': 'server',
             'count': models.Category.objects.get(name='虛擬機').asset_set.all().count(), 'color': '#ff9900'},
            {'title': '網路設備', 'icon': 'cloud',
             'count': models.Category.objects.get(name='網路設備').asset_set.all().count(), 'color': '#19be6b'},
            {'title': '總數', 'icon': 'box', 'count': models.Asset.objects.all().count(), 'color': '#ed3f14'}
        ]

        return counts

    def get(self, request):

        list_week_day = list(self.recent_seven_days())
        list_week_day.reverse()

        asset_data = {
            'label': [i.strftime('%Y-%m-%d') for i in list_week_day],
            'latest_data': [],
            'create_data': []

        }

        for d in list_week_day:
            asset_data['latest_data'].append(random.choice(list(range(1, 10))))
            asset_data['create_data'].append(random.choice(list(range(1, 10))))

        asset_type = {
            'label': ["服務器", "虛擬機", "網路設備"],
            'data': [
                models.Category.objects.get(name='服務器').asset_set.all().count(),
                models.Category.objects.get(name='虛擬機').asset_set.all().count(),
                models.Category.objects.get(name='網路設備').asset_set.all().count()
            ]
        }



        data = {
            'asset_data': asset_data,
            'count': self.get_count(),
            'asset_type': asset_type
        }

        return Response(data)
