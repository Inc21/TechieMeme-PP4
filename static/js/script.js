var cardCarousel = document.querySelector('#carouselExampleControls')

if(window.matchMedia("(min-width: 768px)").matches){
    var carousel = new bootstrap.Carousel(cardCarousel, {
        interval: false,
      });

    var carouselWidth = $(".carousel-inner")[0].scrollWidth; // Get the width of the carousel
    var cardWidth = $(".carousel-item").width(); // Get the width of a card

    var scrollPosition = 0; // Init the scroll position

    $(".carousel-control-next").on("click", function () {
        if (scrollPosition < (carouselWidth - (cardWidth * 4))) { //check if you can go any further
            scrollPosition = scrollPosition + cardWidth;  //update scroll position
            $(".carousel-inner").animate({ scrollLeft: scrollPosition },600); //scroll left
        }
    });
    $(".carousel-control-prev").on("click", function () {
        if (scrollPosition > 0) { //check if you can go any further
            scrollPosition = scrollPosition - cardWidth;  //update scroll position
            $(".carousel-inner").animate({ scrollLeft: scrollPosition },600); //scroll left
        }
    });
} else {
    $(cardCarousel).addClass("slide");
}

