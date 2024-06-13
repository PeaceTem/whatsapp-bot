// Name of the database and object store
const dbName = 'model-storage';
const storeName = 'contact';

// Open a connection to the IndexedDB database
let request = indexedDB.open(dbName);

request.onerror = function(event) {
  console.error('Database error:', event.target.error);
};
var records;
request.onsuccess = function(event) {
  let db = event.target.result;
  console.log('Database opened successfully');

  // Start a new transaction
  let transaction = db.transaction(storeName, 'readonly');
  let objectStore = transaction.objectStore(storeName);

  // Retrieve all records from the object store
  let getAllRequest = objectStore.getAll();

  getAllRequest.onerror = function(event) {
    console.error('Error retrieving data:', event.target.error);
  };

  getAllRequest.onsuccess = function(event) {
    records = event.target.result;
    console.log('Data retrieved successfully:', records);
  };
};


function downloadObjectAsJson(object, filename) {
    // Convert object to JSON string
    const jsonString = JSON.stringify(object, null, 2);

    // Create a blob from the JSON string
    // const blob = new Blob([jsonString], { type: 'text/csv' });
    const blob = new Blob([jsonString], { type: 'application/json' });

    // Create a URL for the blob

    const url = URL.createObjectURL(blob);

    // Create a link to trigger the download
    const a = document.createElement('a');
    a.setAttribute('hidden', '');
    a.setAttribute('href', url);
    a.setAttribute('download', filename);

    // Append the link, trigger the download, and remove the link
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
};

downloadObjectAsJson(records, 'wa_contacts.json');