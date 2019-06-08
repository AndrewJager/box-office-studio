function runDatepicker(curDate, dates){
    jQuery(document).ready(function() {
            
        var holidays = {};
        var i;
        for (i = 0; i <= 100; i++)
        {
            var year = '20' + i.toString().padStart(2, '0');
            holidays[ new Date( '6/20/' + year )] = new Date( '6/20/' + year).toString(); 
            holidays[ new Date( '6/25/' + year )] = new Date( '6/25/' + year).toString();   
        }
       console.log(holidays);
        let datesArray = dates.replace('[','').replace(']','').split(",").map(String);
        var movieDates = {}
        for (i = 0; i < datesArray.length; i++)
        {
            datesArray[i] = datesArray[i].trim()
            movieDates[ new Date( datesArray[i])] = new Date ( datesArray[i] ).toString();
        }
        console.log(movieDates);
        jQuery('#calendar').datepicker({
            beforeShowDay: function( date ) {
                var highlight = holidays[date];
                var movieHightlight = movieDates[date];
                if( highlight ) {
                    return [true, "holidayDate", highlight];
                } 
                else if (movieHightlight){
                    return [true, "movieDate", movieHightlight];
                } else {
                    return [true, '', ''];
                }
            },
            dateFormat: "yy-mm-dd",
            changeYear: true,
            numberOfMonths: 3,
            defaultDate: curDate,
        });
    });
}