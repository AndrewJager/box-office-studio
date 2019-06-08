function runDatepicker(curDate, dates){
    jQuery(document).ready(function() {
            
        var holidays = {};
        var i;
        for (i = 0; i <= 100; i++)
        {
            var year = '20' + i.toString().padStart(2, '0');
            holidays[ new Date( '6/21/' + year )] = new Date( '6/20/' + year).toString(); 
            holidays[ new Date( '6/25/' + year )] = new Date( '6/25/' + year).toString();   
        }
        let datesArray = dates.replace('[','').replace(']','').split(",").map(String);
        var movieDates = {}
        for (i = 0; i < datesArray.length; i++)
        {
            datesArray[i] = datesArray[i].trim()
            movieDates[ new Date( datesArray[i])] = new Date ( datesArray[i] ).toString();
        }
        jQuery('#calendar').datepicker({
            beforeShowDay: function( date ) {
                var holidayHighlight = holidays[date];
                var movieHightlight = movieDates[date];
                var day = date.getDay();
                if (movieHightlight){ //Highlight days with movies scheduled
                    return [true, "movieDate", movieHightlight];
                } 
                else if (holidayHighlight) { //Highlight holidays
                    return [true, "holidayDate", holidayHighlight];
                } 
                if (day == 5) { //Highlight Fridays
                    return [true, "fridayDate", movieHightlight];
                } else {
                    return [true, '', ''];
                }
            },
            dateFormat: "yy-mm-dd",
            changeYear: true,
            numberOfMonths: 3,
            defaultDate: curDate,
            minDate: curDate,
        });
    });
}