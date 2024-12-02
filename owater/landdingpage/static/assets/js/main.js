$(function () {
    window.onscroll = function () { fun_fix_header() };
    var header = document.getElementById("header");
    var sticky = header.offsetTop;

    // Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
    function fun_fix_header() {
        if (window.pageYOffset > sticky) {
            header.classList.add("sticky-header");
        } else {
            header.classList.remove("sticky-header");
        }
    }


    $("#show-more").click(function (e) {
        $("#about-more").slideToggle("slow");
        $(this).hide();
    })


    $(".menu-scrollTop a").click(function (e) {
        e.stopPropagation();
        var e_id = $(this).attr("href");
        console.log(e_id);
        $('html,body').animate({ scrollTop: ($(e_id).offset().top - $("#header").height()) }, 'slow');
    });


    //mobile_menu_trigger
    $('.mobile_menu_trigger').click(function () {
        $(this).find('.nav-icon').toggleClass('active');
        $(".wrap-menu").toggleClass('active');
        $('body').toggleClass('expand-menu');
        header.classList.remove("sticky-header");
    });
    $('.wrap-menu').click(function () {
        $(this).toggleClass('active');
    });
    $('.wrap-m-menu').click(function (e) {
        e.stopPropagation();
    });

    $(".wrap-menu .close-mm").click(function (e) {
        $(".mobile_menu_trigger .nav-icon").toggleClass("active");
        $(".wrap-menu").toggleClass('active');
        e.stopPropagation();
    })

    $('#menu li').bind().click(function (e) {
        $(this).toggleClass("open").find('> ul').stop(true, true).slideToggle(500).end().siblings().find('ul').slideUp().parent().removeClass("open");
        e.stopPropagation();
    });
    $('#menu  a').click(function (e) {
        e.stopPropagation();
    });

    $('.sidebar-menu li').bind().click(function (e) {
        $(this).toggleClass("open").find('.sub').stop(true, true).slideToggle(500).end().siblings().find('.sub').slideUp().parent().removeClass("open");
        e.stopPropagation();
    });
    $('.sidebar-menu li a').click(function (e) {
        e.stopPropagation();
    });




    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }
    });
    $('#back-to-top').click(function (e) {
        e.stopPropagation();
        $('html,body').animate({ scrollTop: 0 }, 'slow');
    });

});
function numberFormatInput(input) {
	const value = input.value.trim();
	const cleanedValue = value.replace(/[^\d,.-]/g, "");
	const cleanedValueWithComma = cleanedValue.replace(/(,)(?=\d*\.\d*$)/g, "");
	const valueSet = parseFloat(cleanedValueWithComma.replace(/,/g, ""));
	if (!isNaN(valueSet) && isFinite(valueSet) && value !== "") {
		input.value = valueSet;
	} else {
		input.value = "";
	}
}