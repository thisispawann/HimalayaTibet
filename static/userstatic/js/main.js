$(document).ready(function () {
    $(window).scrollTop(0);

    priceSlider();
});

$(function () {
    $(window).scroll(function () {
        if ($(window).scrollTop() <= 40) {
            $('.navbar-wrapper').removeClass('navbar-scroll');
        } else {
            $('.navbar-wrapper').addClass('navbar-scroll');
        }
    });
});

window.scrollBy({
    top: 100,
    left: 0,
    behavior: 'smooth'
});


//filter sidebar

$(".filter-card #price input:checkbox").on("click", function(){
    var $box = $(this);
    if ($box.is(":checked")) {
        var group = "input:checkbox[name='" + $box.attr("name") + "']";
        $(group).prop("checked", false);
        $box.prop("checked", true);
    } else {
        $box.prop("checked", false);
    }
});

function priceSlider(){
    const slider = $('#sliderPrice');
    const rangeMin = parseInt(slider.data('min'));
    const rangeMax = parseInt(slider.data('max'));
    const step = parseInt(slider.data('step'));
    const filterInputs = $('.price-range input');

    noUiSlider.create(slider[0], {
        start: [rangeMin, rangeMax],
        connect: true,
        step: step,
        range: {
            'min': rangeMin,
            'max': rangeMax
        },

        // make numbers whole
        format: {
            to: value => value,
            from: value => value
        }
    });

    // bind inputs with noUiSlider 
    slider[0].noUiSlider.on('update', (values, handle) => {
        // console.log(values, handle)
        filterInputs[handle].value = values[handle];
    });

    $.each(filterInputs, (indexInput, input) => {
        $(filterInputs[indexInput]).on('change', () => {
            slider[0].noUiSlider.setHandle(indexInput, input.value);
        })
    });
}


