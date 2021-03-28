(function($)
{"use strict"
$(window).on('scroll',function(){var scroll=$(window).scrollTop();if(scroll<400){$(".header-sticky").removeClass("sticky-bar");$('#back-top').fadeOut(500);}else{$(".header-sticky").addClass("sticky-bar");$('#back-top').fadeIn(500);}});$('#back-top a').on("click",function(){$('body,html').animate({scrollTop:0},800);return false;});var menu=$('ul#navigation');if(menu.length){menu.slicknav({prependTo:".mobile_menu",closedSymbol:'+',openedSymbol:'-'});};function mainSlider(){var BasicSlider=$('.slider-active');BasicSlider.on('init',function(e,slick){var $firstAnimatingElements=$('.single-slider:first-child').find('[data-animation]');doAnimations($firstAnimatingElements);});BasicSlider.on('beforeChange',function(e,slick,currentSlide,nextSlide){var $animatingElements=$('.single-slider[data-slick-index="'+nextSlide+'"]').find('[data-animation]');doAnimations($animatingElements);});BasicSlider.slick({autoplay:true,autoplaySpeed:8000,dots:true,fade:true,arrows:false,dots:false,prevArrow:'<button type="button" class="slick-prev"><i class="ti-angle-left"></i></button>',nextArrow:'<button type="button" class="slick-next"><i class="ti-angle-right"></i></button>',responsive:[{breakpoint:1024,settings:{slidesToShow:1,slidesToScroll:1,infinite:true,}},{breakpoint:991,settings:{slidesToShow:1,slidesToScroll:1,arrows:false}},{breakpoint:767,settings:{slidesToShow:1,slidesToScroll:1,arrows:false,dots:false}}]});function doAnimations(elements){var animationEndEvents='webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';elements.each(function(){var $this=$(this);var $animationDelay=$this.data('delay');var $animationType='animated '+$this.data('animation');$this.css({'animation-delay':$animationDelay,'-webkit-animation-delay':$animationDelay});$this.addClass($animationType).one(animationEndEvents,function(){$this.removeClass($animationType);});});}}
mainSlider();$('.directory-active').slick({dots:false,infinite:true,autoplay:true,speed:400,arrows:true,prevArrow:'<button type="button" class="slick-prev"><i class="fas fa-chevron-left"></i></button>',nextArrow:'<button type="button" class="slick-next"><i class="fas fa-chevron-right"></i></button>',slidesToShow:4,slidesToScroll:1,responsive:[{breakpoint:1400,settings:{slidesToShow:3,slidesToScroll:1,infinite:true,dots:false,}},{breakpoint:1024,settings:{slidesToShow:2,slidesToScroll:1,infinite:true,dots:false,}},{breakpoint:992,settings:{slidesToShow:2,slidesToScroll:1,infinite:true,dots:false,}},{breakpoint:768,settings:{slidesToShow:1,slidesToScroll:1,arrows:false}},{breakpoint:480,settings:{slidesToShow:1,slidesToScroll:1,arrows:false}},]});var testimonial=$('.h1-testimonial-active');if(testimonial.length){testimonial.slick({dots:false,infinite:true,speed:1000,autoplay:false,arrows:true,prevArrow:'<button type="button" class="slick-prev"><i class="ti-angle-left"></i></button>',nextArrow:'<button type="button" class="slick-next"><i class="ti-angle-right"></i></button>',slidesToShow:1,slidesToScroll:1,responsive:[{breakpoint:1024,settings:{slidesToShow:1,slidesToScroll:1,infinite:true,dots:false,arrows:true}},{breakpoint:600,settings:{slidesToShow:1,slidesToScroll:1,dots:false,arrows:false}},{breakpoint:480,settings:{slidesToShow:1,slidesToScroll:1,dots:false,arrows:false}}]});}
$('.brand-active').slick({dots:false,infinite:true,autoplay:true,speed:400,arrows:false,slidesToShow:4,slidesToScroll:1,responsive:[{breakpoint:1024,settings:{slidesToShow:4,slidesToScroll:3,infinite:true,dots:false,}},{breakpoint:992,settings:{slidesToShow:3,slidesToScroll:1,infinite:true,dots:false,}},{breakpoint:768,settings:{slidesToShow:2,slidesToScroll:1}},{breakpoint:480,settings:{slidesToShow:1,slidesToScroll:1}}]});var nice_Select=$('select');if(nice_Select.length){nice_Select.niceSelect();}
$("[data-background]").each(function(){$(this).css("background-image","url("+$(this).attr("data-background")+")")});new WOW().init();function mailChimp(){$('#mc_embed_signup').find('form').ajaxChimp();}
mailChimp();var popUp=$('.single_gallery_part, .img-pop-up');if(popUp.length){popUp.magnificPopup({type:'image',gallery:{enabled:true}});}
var popUp=$('.popup-video');if(popUp.length){popUp.magnificPopup({type:'iframe'});12;;}
$('.counter').counterUp({delay:10,time:3000});})(jQuery);

var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}