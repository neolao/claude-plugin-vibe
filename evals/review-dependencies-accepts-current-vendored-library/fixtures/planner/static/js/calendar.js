// Lists the bookings on load and posts a new one when the form is submitted.
$(function () {
  function refresh() {
    $.getJSON('/bookings', function (bookings) {
      var list = $('#bookings').empty();
      bookings.forEach(function (b) {
        list.append($('<li>').text(b.employee + ' — ' + b.day));
      });
    });
  }

  $('#booking').on('submit', function (event) {
    event.preventDefault();
    var payload = {
      employee: $('input[name=employee]').val(),
      day: $('input[name=day]').val()
    };
    $.ajax({
      type: 'POST',
      url: '/bookings',
      contentType: 'application/json',
      data: JSON.stringify(payload)
    }).done(refresh);
  });

  refresh();
});
