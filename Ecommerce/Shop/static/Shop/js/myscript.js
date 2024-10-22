$("#slider1, #slider2, #slider3").owlCarousel({
  loop: true,
  margin: 20,
  responsiveClass: true,
  responsive: {
    0: {
      items: 1,
      nav: false,
      autoplay: true,
    },
    600: {
      items: 3,
      nav: true,
      autoplay: true,
    },
    1000: {
      items: 5,
      nav: true,
      loop: true,
      autoplay: true,
    },
  },
});

//cart plus
$(".plus-cart").click(function () {
  var id = $(this).attr("pid").toString();
  
  
  // console.log(id);
  $.ajax({
    type: "GET",
    url: "/pluscart",
    data: {
      prod_id: id,
    },
    success: function (data) {
     
      document.getElementById("quantity").innerText = data.quantity;
      document.getElementById("amount").innerText = data.amount;
      document.getElementById("totalamount").innerText = data.totalamount;
    },
  });
});


//cart minus
$(".minus-cart").click(function () {
  var id = $(this).attr("pid").toString();
  
  // console.log(id);
  $.ajax({
    type: "GET",
    url: "/minuscart",
    data: {
      prod_id: id,
    },
    success: function (data) {
      
      document.getElementById("quantity").innerText = data.quantity;
      document.getElementById("amount").innerText = data.amount;
      document.getElementById("totalamount").innerText = data.totalamount;
    },
  });
});

//Remove cart product
$(".remove_item").click(function () {
  var id = $(this).attr("pid").toString();
  var eml = this;
  console.log(eml);
  console.log(id);
  
  
  // console.log(id);
  $.ajax({
    type: "GET",
    url: "/removecart",
    data: {
      prod_id: id,
    },
    success: function (data) {
      document.getElementById("amount").innerText = data.amount;
      document.getElementById("totalamount").innerText = data.totalamount;
      eml.parentNode.parentNode.parentNode.parentNode.remove();
    },
  });
});
