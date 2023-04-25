const csvFilePath = '../database/beermeal.csv';
// Define the column to extract
Papa.parse(csvFilePath, {
    download: true,
    header: true,
    complete: function (results) {
        const container = document.getElementById('container');
        const groups = new Map();

        // const groups2 = new Map();

        results.data.forEach(function (row) {
            //taking rows
            const beerType = row['beertype'];
            if (!groups.has(beerType)) {
                groups.set(beerType, []);
            }
            groups.get(beerType).push(row);
        });


        //for meals
        groups.forEach(function (rows, beerType) {
            const mealList = rows.map(function (row) {
                const mealPhoto = row['meal_photourl'];
                return `<li><img src="${mealPhoto}" alt="${row['meal']}"><span>${row['meal']}</span></li>`;
            }).join('');
            
            const beerPhoto = rows[0]['photourl'];
            const beerPageContents = `
                <div id="content">
                    <img id="ellipse" src="../src/Ellipse 6.png">
                    <div id="left">
                        <img src="${beerPhoto}" alt="${beerType}">
                    </div>
                    <div id="right">
                        <h1 id="beerType">${beerType}</h1>
                        <p>${rows[0]['beer_description']}</p>
                        <button onclick="window.location.reload()">повернутися до сортів</button>
                    </div>
                </div>
                <div id ="bottom">
                    <h1 id="beerType">з чим поєднюється</h1>
                    <ul>
                        ${mealList}
                    </ul>
                </div>
            `;
            const link = document.createElement('a');
            link.href = '#';
            link.innerHTML = 'ПЕРЕЙТИ';
            link.addEventListener('click', function (event) {
                event.preventDefault();
                container.innerHTML = beerPageContents;
                container.scrollTop = 0;
            });
            const beerDiv = document.createElement('div');
            beerDiv.id = 'card';
            const beerIMG = document.createElement('img');
            beerIMG.id = 'photo';
            beerIMG.src = beerPhoto;

            const beerName = document.createElement('p');
            beerName.id = 'beerName';
            beerName.innerHTML = beerType;
            beerDiv.appendChild(beerIMG);
            beerDiv.appendChild(beerName);
            beerDiv.appendChild(link);
            container.appendChild(beerDiv);
        });
    }
});