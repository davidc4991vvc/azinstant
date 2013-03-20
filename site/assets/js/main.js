
(function($) {

$('#searchbox').keyup(function(){

  var url = 'http://127.0.0.1:5000/search';
  var q = '';'' 

  q = $("#searchbox").val();
  if (q.length == 0) {
    $("#q").focus();
  } else {
    url +='?q=' + q;
  }

  var resultsDiv = $('#results');

  if (resultsDiv.children().length > 0) {
    resultsDiv.children().remove();
  }
  $.ajax({
    type: 'GET',
    url: url,
    async: true,
    // contentType: "application/json",
    dataType: 'jsonp',
    // jsonpCallback: 'azinstant',
    success: function(json) {
      azinstant;
      console.log('call success');
    },
    error: function(data) {
       console.log('error', data);
    }
  });
});

})(jQuery);

azinstant = function(data) {

  var result = data;

  var query = result.query;
  console.log('callback for query', query);

  var source = $("#search-item").html();
  var template = Handlebars.compile(source);
  
  var resultsDiv = $('#results');
  resultsDiv.append(template(result));

};