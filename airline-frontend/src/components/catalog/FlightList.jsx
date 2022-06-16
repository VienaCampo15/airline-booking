import React, { useState, useEffect } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Container from '@mui/material/Container'

export default function FlightList(){

    const initialList = [ ];
    const [FlightsList, setList] = useState(initialList);

    useEffect(() => {
        async function fetchFlights(){
            try {
                const response = await fetch("https://airline-app.azurewebsites.net/catalog/all");
                if (response.ok){
                    const flights = await response.json();
                    setList(flights);
                }
            }catch(err) {
                console.log("Petición fallida.");
            }
        }
        fetchFlights();
    }, []);
    

    return (<>
            <Container maxWidth="bd">
                <TableContainer component={Paper} sx={{mt:'3rem'}}>
                    <Table aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell align="center">Flight Number</TableCell>
                                <TableCell align="center">Departure Date</TableCell>
                                <TableCell align="center">Departure Airport Code</TableCell>
                                <TableCell align="center">Departure Airport Name</TableCell>
                                <TableCell align="center">Arrival Airport Code</TableCell>
                                <TableCell align="center">Arrival Airport Name</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {
                                FlightsList.length > 0 &&
                                FlightsList.map(flight => (
                                    <TableRow key={flight.id} 
                                    sx={{ '&:last-child td, &:last-child th': { border: 0 }}}>                              
                                        <TableCell component="th" scope="row" align="center">
                                            {flight.flightNumber}
                                        </TableCell>
                                        <TableCell align="center">{new Date(flight.departureDate).toDateString()}</TableCell>
                                        <TableCell align="center">{flight.departureAirportCode}</TableCell>
                                        <TableCell align="center">{flight.departureAirportName}</TableCell>
                                        <TableCell align="center">{flight.arrivalAirportCode}</TableCell>
                                        <TableCell align="center">{flight.arrivalAirportName}</TableCell>
                                    </TableRow>
                                ))                            
                            }
                        </TableBody>
                    </Table>
                </TableContainer>
            </Container>
        </>
    )
}