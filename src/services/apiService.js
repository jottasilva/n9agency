import axios from 'axios';
export const url_api = 'https://37ed-170-233-6-221.ngrok-free.app';
const apiClient = axios.create({
        baseURL:url_api,
        timeout:10000,
        headers:{
            'Content-Type':'application/json',
        },
});
apiClient.interceptors.response.use(
    (response) => response,
    (error) => {
        console.log('Erro na Api :', error.response);
        return Promise.reject(error);
});
// Router Methods
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
