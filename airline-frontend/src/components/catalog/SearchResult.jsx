import { Box, Container, Grid, TextField, Typography, AppBar, Toolbar } from '@mui/material'
import { LocalizationProvider, MobileDatePicker } from '@mui/x-date-pickers'
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns'
import React from 'react'
import SearchCard from './SearchCard'

const SearchResult = (props) => {
  
  const handleChange = () => {};

  const getTime = date => {
    const time = date.toISOString().substring(11,16);
    return time;
  }

  const HoursAndMinsDiff = (date1, date2) => {
    let date1h = parseInt(date1.getHours());
    let date2h = parseInt(date2.getHours());
    let hoursdiff = date1h > date2h ? date1h-date2h : date2h-date1h;

    let date1m = parseInt(date1.getMinutes());
    let date2m = parseInt(date2.getMinutes());
    let minsdiff = date1m > date2m ? date1m-date2m : date2m-date1m;

    const diff = `${hoursdiff}h ${minsdiff}m`;

    return diff;
  };

  const searchresult = props.results.map((flight,id) => <SearchCard key={id} departureAirportTime={getTime(new Date(flight.departureDate))}
                                                            arrivalAirportTime={getTime(new Date(flight.arrivalDate))}
                                                            departureAirportCode={flight.departureAirportCode}
                                                            arrivalAirportCode={flight.arrivalAirportCode}
                                                            flightTime={HoursAndMinsDiff(new Date(flight.departureDate), new Date(flight.arrivalDate))}
                                                            ticketCurrency={flight.ticketCurrency}
                                                            ticketPrice={flight.ticketPrice}
                                                            flightNumber={flight.flightNumber}/>
                                                          );
  console.log(searchresult[0])

  return (
    <div>
      <AppBar position="fixed" sx={{display:{xs:'none', sm:'block'}, mt:7.8, bgcolor:'transparent', boxShadow:'none'}}>
        <Toolbar disableGutters>
          <Grid container sx={{bgcolor:'#d2b7e5', pt:1, pb:0.5, boxShadow:1}} >
            <Grid item xs={1} />
            <Grid item xs={1} sx={{display:'flex', justifyContent:'center', alignItems:'center'}} >
              <TextField label="From" variant="standard" color='secondary' size='normal' disabled 
                         defaultValue={props.results[0].departureAirportCode} />
            </Grid>
            <Grid item xs={0.5} />
            <Grid item xs={1} sx={{display:'flex', justifyContent:'center', alignItems:'center'}} >
              <TextField label="To" variant="standard" color='secondary' size='normal' disabled 
                         defaultValue={props.results[0].arrivalAirportCode} />
            </Grid>
            <Grid item xs={0.5} />
            <Grid item xs={1.5} sx={{display:'flex', justifyContent:'center', alignItems:'center'}} >
              <LocalizationProvider dateAdapter={AdapterDateFns}>
                <MobileDatePicker
                  sx={{color:'#5A189A'}}
                  label="Date"
                  inputFormat='EE, d MMM'
                  disabled
                  value={props.results[0].departureDate}
                  onChange={handleChange}
                  renderInput={(params) => <TextField label="To" variant="standard" color='secondary' size='normal' {...params} />}
                />
              </LocalizationProvider>
            </Grid>
            <Grid item flexGrow={1}/>
          
          </Grid>

        </Toolbar>
      </AppBar>
      
      <Toolbar sx={{mb:'2rem'}}/>

      <Container maxWidth="sm">
        <Box sx={{bgcolor:'#d2b7e5', borderRadius:4, boxShadow:3, mb:'1rem', pb:'1rem'}}>
          <Typography variant='h3' component='h3' sx={{textAlign:'center', py:'2rem', color:'#240046'}}>
            Select your flight
          </Typography>

          {
            searchresult.length > 0 ? searchresult : (
            <Typography variant='h4' component='h4' sx={{textAlign:'center', py:'2rem', color:'#240046'}}>
              NOT EXISTING FLIGHTS.
            </Typography>
            )
          }
          
        </Box>
      </Container>
    </div>
  )
}

export default SearchResult