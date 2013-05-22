


var gDir = {

    initSearchAutoComplete: function(url) {
        $('.search-query').typeahead({
            source: function(query, process) {
                $.getJSON(url + "?q=" + encodeURI(query), process);
            },
            minLength: 3
        });
    },

    dummyfunc: function() {}
};



