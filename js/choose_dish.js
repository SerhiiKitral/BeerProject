const csvFilePath = '../database/beermeal.csv';

const mealColumn = 'meal';

let data = [];

Papa.parse(csvFilePath, {
    download: true,
    header: true,
    complete: function (results) {
        data = results.data;
    }
});

function autocompleteMatch(input) {
    if (input == '') {
        showResults();
    }
    const reg = new RegExp(input, 'i');
    const uniqueMeals = new Set();
    return data.filter(function (row) {
        return row[mealColumn] && row[mealColumn].match(reg);
    }).filter(function(row) {
        // Only keep unique meals
        if (uniqueMeals.has(row[mealColumn])) {
            return false;
        } else {
            uniqueMeals.add(row[mealColumn]);
            return true;
        }
    });
}

function showResults(val) {
    const result = document.getElementById("result");
    result.innerHTML = '';
    let list = '';
    const terms = autocompleteMatch(val);
    for (let i = 0; i < terms.length; i++) {
        list +=
        '<li><a href="#link-to" class="mealLi" data-index="' + i + '">' + terms[i][mealColumn] + '</a></li>';
    }
    result.innerHTML = list;
    const mealLinks = document.querySelectorAll('.mealLi');
    mealLinks.forEach(function(mealLink) {
        mealLink.addEventListener('click', function (event) {
            event.preventDefault();
            const index = parseInt(this.getAttribute('data-index'));
            showMealPage(terms[index]);
            document.getElementById('link-to').scrollIntoView();
        });
    });
}

function showMealPage(row) {
    const mealdata = document.getElementById("mealdata");
    const meal = row[mealColumn];
    const beerTypes = data.filter(function (row) {
        return row[mealColumn] == meal && row['beertype'] && row['beer_description'] && row['photourl'];
    }).map(function (row) {
        return '<li>' + '<div id="beerText"><h2>' + row['beertype'] + '</h2>' + '<p id="beerDescriptions">' + row['beer_description'] + '</p><a href="where buy.html" id="where_buy" >купити</a></div><div id="beerPhoto"><img src="' + row['photourl'] + '" id="beerPhoto"></div></li>';
    }).join('');

    

    const mealPageContents = '<div id="mealContent"><div id="left">' + '<h1>' + meal + '</h1><img src="' + row['meal_photourl'] + '" id="mealPhoto"></div>' + 
                            '<div id="right"><ul>' + beerTypes + '</ul></div>' +
                            '<img src="../src/Ellipse 71.png" id="ellipse2"></div>';
    mealdata.innerHTML = mealPageContents;
}