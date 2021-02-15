class InstrouctionDV(DetailView):
    model = Instrouction
    ## defatul : templates/app_name/model_detail
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # object 만들어낸다.
        context['object_list'] = Instrouction.objects.all()
        return context
