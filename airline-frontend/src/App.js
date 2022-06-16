import React, { useState } from 'react';
import './App.css'
import { Route, Routes, useNavigate } from 'react-router-dom'
import FlightList from './components/catalog/FlightList'
import FlightSearch from './components/catalog/FlightSearch'
import SearchResult from './components/catalog/SearchResult'
import NavBar from './components/NavegationBar'


function App() {

  const[results, setResults] = useState([]);
  const navigate = useNavigate();

  async function fetchFlightsSearch(departureAirport, arrivalAirport, departureDate){
    console.log(departureAirport);
    console.log(arrivalAirport);
    console.log(departureDate);
    if(departureAirport === '' && arrivalAirport === ''){
      alert("Please, fill in all fields.")
    } else {
        try{
          const response = await fetch(`https://airline-app.azurewebsites.net/catalog/?departureAirportCode=${departureAirport}&arrivalAirportCode=${arrivalAirport}&departureDate=${departureDate}`);
          if(response.ok){
          const flights = await response.json();
          console.log(flights);
          setResults(flights);
          navigate('/catalog/search');
          }
        } catch(error){
          alert("No flights found")
        }
     }
    };

  return (
    <div className = "Airline Nav">
      <NavBar/>
      <Routes>
        <Route path="/" element={<h1>WELCOME TO AIRLINE NORTE-SUR</h1>} />
        <Route path="/catalog" element={<FlightSearch fetchFlightsSearch={fetchFlightsSearch}/>}/>
        <Route path="/catalog/search" element={<SearchResult results={results}/>}/>
        <Route path="/catalog/all" element={<FlightList/>}/>
        <Route path="*" element={<h1>Page Not Found. Sorry :(</h1>} />
      </Routes>
    </div>
  );
}

export default App;
