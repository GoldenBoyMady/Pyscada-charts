cat  = 0;

$( document ).ready(function() {

$.each($('.chartD3-container'),function(key,val){
  // get identifier of the chart
  id = val.id.substring(16);

  // add a new Plot
  cat = $(val).data('categories');
  console.log($(val).data('categories'));
});

});