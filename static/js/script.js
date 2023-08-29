var cardCarousel = document.querySelector('#carouselExampleControls')


    var carousel = new bootstrap.Carousel(cardCarousel, {
        interval: false,
        wrap: true
      });
    
    

    var carouselWidth = $(".carousel-inner")[0].scrollWidth; // Get the width of the carousel
    var cardWidth = $(".small-card").width(); // Get the width of a card

    var scrollPosition = 0; // Init the scroll position
    var prevBtn = document.querySelector(".carousel-control-prev");

    if (scrollPosition == 0) {
        prevBtn.classList.add("invisible");
    } else{
        prevBtn.classList.remove("invisible");
    }
    

    $(".carousel-control-next").on("click", function () {
        // if (scrollPosition < (carouselWidth - (cardWidth * 4))) { //check if you can go any further
        var cardAmount = $(".small-card").length;
        var prevBtn = document.querySelector(".carousel-control-prev");
        var nextBtn = document.querySelector(".carousel-control-next");
        if (scrollPosition < (carouselWidth - (cardWidth * 4)) ) {
            prevBtn.classList.remove("invisible");
         };
         if (scrollPosition > (carouselWidth - (cardWidth * cardAmount) + cardWidth)) { //check if you can go any further )) {
            nextBtn.classList.add("invisible");
         };
            scrollPosition = scrollPosition + cardWidth;  //update scroll position
            $(".carousel-inner").animate({ scrollLeft: scrollPosition },600); //scroll left
        
    });
    $(".carousel-control-prev").on("click", function () {
        var prevBtn = document.querySelector(".carousel-control-prev");
        var nextBtn = document.querySelector(".carousel-control-next");
        if (scrollPosition == 0 + cardWidth) { //check if you can go any further
            prevBtn.classList.add("invisible");
        };
        if (scrollPosition < (carouselWidth - cardWidth)) { //check if you can go any further )) {
            nextBtn.classList.remove("invisible");
         };
            scrollPosition = scrollPosition - cardWidth;  //update scroll position
            $(".carousel-inner").animate({ scrollLeft: scrollPosition },600); //scroll left
    });


