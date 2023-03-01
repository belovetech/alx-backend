import { print, createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (err) =>
  console.log(`Redis client not connected to the server: ${err}`)
);

client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
}

const clientGET = promisify(client.GET);
async function displaySchoolValue(schoolName) {
  const value = await clientGET.bind(client)(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton').catch((err) => console.log(err));
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
