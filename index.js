const http = require('http');
const port = 80;
const unused = "i am an unused variable";

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello from Node.js Docker!');
});

server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});