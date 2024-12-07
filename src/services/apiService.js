import axios from 'axios';

export const url_api = 'https://200b-170-233-6-221.ngrok-free.app';
const apiClient = axios.create({
    baseURL: url_api,
    timeout: 10000,
    headers: {
        'Content-Type': 'application/json',
    },
    withCredentials: true
});

apiClient.interceptors.response.use(
    (response) => response,
    (error) => {
        if (error.response && error.response.status === 403) {
            console.log('Erro CORS: Permissão negada. Verifique o servidor.');
        } else {
            console.log('Erro na API:', error.response);
        }
        return Promise.reject(error);
    }
);

const getInfo = () => apiClient.get('/config');
const getIdea = () => apiClient.get('/ideas');
const getPortfolio = () => apiClient.get('/clients');
const getArchives = (email) => apiClient.get('/archives?email=' + email);

export default {
    getInfo,
    getIdea,
    getPortfolio,
    getArchives
};
