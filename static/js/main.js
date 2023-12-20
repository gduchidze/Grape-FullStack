const hamburgerIcon = document.querySelector(".hamburger-icon");
const navigation = document.querySelector(".navigation");

const profileImg = document.querySelector(".profile img");
const profileActions = document.querySelector(".profile__actions");

let flag = true;

hamburgerIcon.addEventListener("click", () => {
  if (!flag) {
    navigation.style.display = "flex";
    flag = true;
  } else {
    navigation.style.display = "none";
    flag = false;
  }
});

let proFlag = false;
profileImg.addEventListener("click", () => {
  if (!proFlag) {
    profileActions.style.display = "flex";
    proFlag = true;
  } else {
    profileActions.style.display = "none";
    proFlag = false;
  }
});

// wines page

const cardDiv = document.querySelector("#card-div");

const product_01 =
  "https://www.topgeorgian.wine/wp-content/uploads/2022/11/WT0089-menabde-wines-khashmis-saperavi-2021.jpg";

const product_02 =
  "https://www.topgeorgian.wine/wp-content/uploads/2022/07/WT0076-khmelos-marani-shavkapito-kasris-2021.jpg";

const product_03 =
  "https://www.topgeorgian.wine/wp-content/uploads/2022/11/QV0138-niamori-chinuri-qvevri-2021-600x600.jpg";

const product_04 =
  "https://www.topgeorgian.wine/wp-content/uploads/2022/11/QV0139-niamori-rkatsiteli-qvevri-2021-600x600.jpg";

const product_05 =
  "https://www.topgeorgian.wine/wp-content/uploads/2022/11/QV0144-niamori-tavkveri-qvevri-2021-600x600.jpg";

const products = [
  {
    id: "01",
    title: "Khashmis Saperavi",
    geoName: "ხაშმის საფერავი",
    price: 27.0,
    imgUrl: product_01,

    category: "dry red",

    desc: ``,
  },

  {
    id: "02",
    title: "Shavkapito",
    geoName: "შავკაპიტო",
    price: 25.0,
    imgUrl: product_02,

    category: "dry red",

    desc: `
    `,
  },

  {
    id: "03",
    title: "Chinuri",
    geoName: "ჩინური",
    price: 22.0,
    imgUrl: product_03,

    category: "dry white",

    desc: `
    `,
  },

  {
    id: "04",
    title: "Rkatsiteli",
    geoName: "რქაწითელი",
    price: 18.0,
    imgUrl: product_04,

    category: "dry white",

    desc: `
    `,
  },

  {
    id: "05",
    title: "Tavkveri",
    geoName: "თავკვერი",
    price: 18.0,
    imgUrl: product_05,

    category: "dry white",

    desc: `
`,
  },
];

function renderCard(changedCard) {
  if (!changedCard || changedCard === "all") {
    cardDiv.innerHTML = "";
    for (let i = 0; i < products.length; i++) {
      let { id, title, geoName, price, imgUrl, category, desc } = products[i];

      cardDiv.innerHTML += `
  <div class="type__card">
    <img src=${imgUrl} alt="card" />
    <div class="type__card-info">
      <h5>${geoName}</h5>
      <p>${desc}</p>
      <p class="type__card-price">${price} ლარი</p>
    </div>
  </div>
    
  `;
    }
  } else {
    cardDiv.innerHTML = "";
    let filteredItem = products.filter((e) => e.category === changedCard);
    if (filteredItem.length === 0) {
      cardDiv.innerHTML = `
      <h1 class='not-found mt-5 mb-5 w-100 d-flex justify-content-center text-light'>No Products are found!</h1>
      `;
    }
    filteredItem.map(
      (item, index) =>
        (cardDiv.innerHTML += `
  <div class="type__card">
    <img src=${item.imgUrl} alt="card" />
    <div class="type__card-info">
      <h5>${item.geoName}</h5>
      <p>${item.desc}</p>
      <p class="type__card-price">${item.price} ლარი</p>
    </div>
  </div>
    
  `)
    );
  }
}

function changeItem() {
  var x = document.getElementById("mySelect").value;
  console.log(x);
  renderCard(x);
}

renderCard();
