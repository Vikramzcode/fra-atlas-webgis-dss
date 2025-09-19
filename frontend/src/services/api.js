import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:5000";


export const getClaims = () => axios.get(`${API_URL}/api/claims`);
export const addClaim = (data) => axios.post(`${API_URL}/api/claims`, data);
