function style_semester_li(semester) {
  return '<a class="semester">' + semester.name + '</a>';
}

function style_section(section) {
  return '<div class="card" data-classcode="' +
             section.class_code + '" data-number="' + section.number + '">' +
           '<div class="card-content">' +
             '<div class="section-header card-title">' +
               section.class_code + ' ' + section.number + ' ' + section.kind +
             '</div>' +
             '<ul class="section-info">' +
               '<li>' + section.instructor + '</li>' +
               '<li>' + section.time + '</li>' +
               '<li>' + (section.days.join('/')) + '</li>' +
               '<li>' + ((section.room != null) ? section.room : '') + '</li>' +
             '</ul>' +
           '</div>' +
         '</div>';
}
