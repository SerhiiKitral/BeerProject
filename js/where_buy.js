const csvFilePath = '../database/ShopProducts.csv';

const beernameColumn = 'beername';
const volumeColumn = 'volume';
const urlColumn = 'url';
const priceColumn = 'price';
const shopColumn = 'shop';
const beertypeColumn = 'beertype';

let data = [];

Papa.parse(csvFilePath, {
    download: true,
    header: true,
    complete: function(results) {
        data = results.data;
        showResults();
    }
});

function autocompleteMatch(input) {
    if (input == '') {
        showResults();
    }
    const reg = new RegExp(input, 'i');
    return data.filter(function(row) {
    return row[beernameColumn] && row[beernameColumn].match(reg);
    }).map(function(row) {
    return { beername: row[beernameColumn], volume: row[volumeColumn], url: row[urlColumn], price: row[priceColumn], shop:row[shopColumn], beertype: row[beertypeColumn]  };
    });
}
function showResults(val) {
    const name = document.getElementById("result");
    name.innerHTML = '';
    let list = '';
    const terms = autocompleteMatch(val);
    for (let i = 0; i < terms.length; i++) {
    list +=
    '<a href="' + terms[i].url + '">' + 
        '<div id="left">' +
            '<div id="name">' + terms[i].beername + '</div>' + 
            '<div id="beertype">' + terms[i].beertype + '</div>' + 
            '<div id="shop">' + terms[i].shop + '</div>' + 
        '</div>' +
        '<div id="right">' +
            '<div id="volume">' + terms[i].volume + '</div>' + 
            '<div id="price">' + terms[i].price + '</div>' + 
        '</div>' +
    '</a>';
    }
    name.innerHTML = list;
}