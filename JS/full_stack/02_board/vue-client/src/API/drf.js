// api/drf.js

export default{
  URL: 'http://localhost:8000/',
  ROUTES: {
    signup: 'rest-auth/signup/',
    login: 'rest-auth/login/',
    logout: 'rest-auth/logout/',
    articles: 'board/articles/',
    article(pk) {
      return `board/articles/${pk}`
    }
  }
}