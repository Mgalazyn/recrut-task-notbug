let persons = [
  {
    id: 1,
    name: "Jan Kowalski"
  }, {
    id: 2,
    name: "John Doe"
  }, {
    id: 3,
    name: "Jarek Kaczka"
  }, {
    id: 4,
    name: "Michal walczak"
  }
];

let ages = [
  {
    person: 1,
    age: 18
  }, {
    person: 2,
    age: 24
  }, {
    person: 3,
    age: 666
  }, {
    person: 4,
    age: 35
  }
];

let locations = [
  {
    person: 1,
    country: "Poland"
  }, {
    person: 2,
    country: "Poland"
  }, {
    person: 3,
    country: "USA"
  }, {
    person: 4,
    country: "Poland"
  }
];


let whole_data = {};


for (let i = 0; i < persons.length; i++) {
  let person = persons[i];
  let personId = person.id;

  let ageObject = ages.find((a) => a.person === personId);
  let age = ageObject ? ageObject.age : null;

  let locationObject = locations.find((l) => l.person === personId);
  let country = locationObject ? locationObject.country : null;

  whole_data[personId] = {
    person,
    age,
    country,
  };
}


// cheking output
console.log(whole_data);


let totalAge = 0;
let count = 0;

for (let key in whole_data) {
  let personData = whole_data[key];
  if (personData.country === "Poland") {
    let age = personData.age;
    if (age) {
      totalAge += age;
      count++;
    }
  }
}

let averageAge = count > 0 ? totalAge / count : null;

// returning avg of ppl from pl
console.log("Average age of people from Poland:", averageAge);




