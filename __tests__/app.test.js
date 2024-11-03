const request = require('supertest');
const app = require('../app');

describe('Express App', () => {
  test('GET / should return Hello World message', async () => {
    const response = await request(app)
      .get('/')
      .expect('Content-Type', /json/)
      .expect(200);

    expect(response.body).toEqual({ message: 'Hello World!' });
  });

  test('GET /api/greet/:name should return personalized greeting', async () => {
    const response = await request(app)
      .get('/api/greet/John')
      .expect('Content-Type', /json/)
      .expect(200);

    expect(response.body).toEqual({ message: 'Hello, John!' });
  });
});