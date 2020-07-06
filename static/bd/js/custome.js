(function($) {
	'use strict';
	jQuery(document).on('ready', function(){
        // START MENU JS
         $(window).on('scroll', function() {
            if ($(this).scrollTop() > 60) {
                $('.header-menu').addClass('shrink');
            } else {
                $('.header-menu').removeClass('shrink');
            }
        });	

        $('.navbar-nav li a').on('click', function(e){
            var anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $(anchor.attr('href')).offset().top - 50
            }, 1500);
            e.preventDefault();
        });

        $('.header-bottom-btn a').on('click', function(e){
          var anchor = $(this);
          $('html, body').stop().animate({
              scrollTop: $(anchor.attr('href')).offset().top - 50
          }, 1500);
          e.preventDefault();
        });

        $(document).on('click','.navbar-collapse.show',function(e) {
        if( $(e.target).is('a') && $(e.target).attr('class') != 'dropdown-toggle' ) {
            $(this).collapse('hide');
        }
        });	

        // Home Slider JS
        $('.home-slider').owlCarousel({
          items:1,
          loop:true,
          dots: true,
          nav:true,
          navText: [
              "<i class='icofont-thin-left'></i>",
              "<i class='icofont-thin-right'></i>"
          ]
        });

        // SERVICE SLIDER
        $('.service-slider').slick({
          dots: true,
          loop:true,
          infinite: true,
          arrows:true,
          prevArrow:"<button type='button' class='slick-prev'><i class='icofont-arrow-left'></i>PREV</button>",
          nextArrow:"<button type='button' class='slick-next'>NEXT<i class='icofont-arrow-right'></i></button>",
          speed: 300,
          slidesToShow: 3,
          slidesToScroll: 2,
          responsive: [
            {
              breakpoint: 1024,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
                infinite: true,
                dots: true
              }
            },
            {
              breakpoint: 600,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2
              }
            },
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1
              }
            }
          ]
        });

        //OUR-CASES SLIDER
        $('.cases-slider').slick({
          dots: false,
          loop:true,
          infinite: true,
          arrows:true,
          prevArrow:"<button type='button' class='slick-prev'><i class='icofont-arrow-left'></i></button>",
          nextArrow:"<button type='button' class='slick-next'><i class='icofont-arrow-right'></i></button>",
          speed: 300,
          slidesToShow: 4,
          slidesToScroll: 2,
          responsive: [
            {
              breakpoint: 1024,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
                infinite: true,
                dots: false
              }
            },
            {
              breakpoint: 600,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2
              }
            },
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1
              }
            }
          ]
        });

        //OUR-CASES SLIDER
        $('.comment-slider').slick({
          dots: false,
          loop:true,
          infinite: true,
          arrows:true,
          prevArrow:"<button type='button' class='slick-prev'><i class='icofont-arrow-left'></i></button>",
          nextArrow:"<button type='button' class='slick-next'><i class='icofont-arrow-right'></i></button>",
          speed: 300,
          slidesToShow: 1,
          slidesToScroll: 1,
          responsive: [
            {
              breakpoint: 1024,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                infinite: true,
                dots: false
              }
            },
            {
              breakpoint: 600,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2
              }
            },
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1
              }
            }
          ]
        });

        //BRAND SLIDER
        $('.brand-slider').slick({
          dots: false,
          loop:true,
          infinite: true,
          arrows:false,
          speed: 300,
          slidesToShow: 6,
          slidesToScroll: 6,
          responsive: [
            {
              breakpoint: 1024,
              settings: {
                slidesToShow: 4,
                slidesToScroll: 1,
                infinite: true,
                dots: false
              }
            },
            {
              breakpoint: 600,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2
              }
            },
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1
              }
            }
          ]
        });

        //NICE SELECT JS
        $(document).ready(function() {
          $('select').niceSelect();
        });

        // WOW JS
        new WOW().init();

        // PRELOADER
        jQuery(window).on('load',function(){
            jQuery(".loader-content").fadeOut(500);
        });

        // BACK TO TOP JS
        $('body').append('<div id="toTop" class="top-btn"><i class="icofont-swoosh-up"></i></div>');
        $(window).scroll(function () {
            if ($(this).scrollTop() != 0) {
                $('#toTop').fadeIn();
            } else {
                $('#toTop').fadeOut();
            }
        }); 
        $('#toTop').click(function(){
            $("html, body").animate({ scrollTop: 0 }, 600);
            return false;
        });

        // MAGNIFIC POPUP MIN JS
        $('.popup-youtube').magnificPopup({
          type: 'iframe',
          index: 'youtube.com/',
          src: '//www.youtube.com/embed/%id%?autoplay=1'
        });
    });
})(jQuery);


  
  
