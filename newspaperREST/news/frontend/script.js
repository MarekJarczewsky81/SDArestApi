// console.log('js działa')


async function logJSONData() {
    const response = await fetch(api_url);
    const jsonData = await response.json();
    console.log();
}

