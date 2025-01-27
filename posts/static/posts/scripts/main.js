$('.main-section__content__texts__write__body__read_more').on('click', function () {
    const read_more = $(this);
    const isExpanded = read_more.attr('aria-expanded') === 'false';
    if (!isExpanded) {
        read_more.find('.button-text').text('Finalizar leitura');
        read_more.children('svg').eq(0).hide()
        read_more.children('svg').eq(1).show();
        read_more.attr('aria-expanded', true)
    } else {
        read_more.find('.button-text').text("Continuar leitura");
        read_more.children('svg').eq(0).show();
        read_more.children('svg').eq(1).hide();
        read_more.attr('aria-expanded', false)
    }
});