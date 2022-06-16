import React, { useState }  from 'react'
import Container from '@mui/material/Container'
import { Avatar, Box, Button, Grid, TextField, Typography } from '@mui/material'
import { LocalizationProvider, MobileDatePicker } from '@mui/x-date-pickers';
import FlightTakeoffIcon from '@mui/icons-material/FlightTakeoff';
import FlightLandIcon from '@mui/icons-material/FlightLand';
import InsertInvitationRoundedIcon from '@mui/icons-material/InsertInvitationRounded';
import ArrowForwardIosRoundedIcon from '@mui/icons-material/ArrowForwardIosRounded';
import {AdapterDateFns} from '@mui/x-date-pickers/AdapterDateFns';


const FlightSearch = (props) => {
  
  const sxbs = {'borderRadius':1,
                'p':1.5, 'color': '#ebedf0',
                'backgroundImage':'linear-gradient(40deg, #284da8, #446bc9, #68419c, #7653a3 )',
                'backgroundSize':'250%', 'transition':'0.5s',
                '&:hover': {'bgcolor':'#3C096C', 'backgroundPosition':'right'}};
  const sxicons = { 'px':1, 'py':1, 'bgcolor':'#284da8', 'boxShadow':2};
  const sxColorIcons = {color:'#edf0f2'}

  const formDataInitial= {departureAirport : '', 
                          arrivalAirport : ''};
  const [formData, setFormData] = useState(formDataInitial);

  const handleInputChange = ev => {
      setFormData(
        {
        ...formData, 
        [ev.target.name] : ev.target.value
      });
  };

  const [date, setDate] = useState(new Date());
  const inputDate = date.toISOString().substring(0,10);

  const handleChange = (newDate) =>{setDate(newDate)};

  return (
    <div>
      <Container maxWidth="sm">
          <Box sx={{bgcolor:'#edf0f2', borderRadius:4, boxShadow:4, mt:'3rem'}}>
              <Typography variant='h3' component='h3' sx={{textAlign:'center', py:'2rem', color:'#173f8a'}}>
                Where next?
              </Typography>
              <Box>
                <Grid container>
                  <Grid item xs={2} sx={{display:'flex', justifyContent:'end', alignItems:'center'}}>
                    <Avatar sx={sxicons}>
                      <FlightTakeoffIcon fontSize='large' sx={sxColorIcons}/>
                    </Avatar>
                  </Grid>
                  <Grid item xs={10}>
                    <TextField required onChange={handleInputChange} id="departureAirport" name="departureAirport"  color='primary' 
                    size='small' variant='filled' label ='Departure airport' sx={{width:'96%', boxShadow:1}} />
                  </Grid>
                  <Grid item xs={12} margin='1rem'/>
                  <Grid item xs={2} sx={{display:'flex', justifyContent:'end', alignItems:'center'}}>
                    <Avatar sx={sxicons}>
                      <FlightLandIcon fontSize='large' sx={sxColorIcons}/>
                    </Avatar>
                  </Grid>
                  <Grid item xs={10}>
                    <TextField required onChange={handleInputChange} id="arrivalAirport" name="arrivalAirport" color='primary' 
                    size='small' variant='filled' label='Arrival airport' sx={{width:'96%', boxShadow:1}} />
                  </Grid>
                  <Grid item xs={12} margin='1rem'/>
                  <Grid item xs={2} sx={{display:'flex', justifyContent:'end', alignItems:'center'}}>
                    <Avatar sx={sxicons}>
                      <InsertInvitationRoundedIcon fontSize='large' sx={sxColorIcons}/>
                    </Avatar>  
                  </Grid>
                  <Grid item xs={10}>
                  <LocalizationProvider dateAdapter={AdapterDateFns}>
                      <MobileDatePicker
                        sx={{color:'#5A189A'}}
                        label="Pick a date"
                        //inputFormat="dd/MM/yyyy"
                        inputFormat='EEEE, MMM d, yyyy'
                        value={date}
                        onChange={handleChange}
                        renderInput={(params) => <TextField required size='small' variant='filled' color='secondary' {...params} sx={{width:'96%', boxShadow:1}}/>}
                      />
                    </LocalizationProvider>
                  </Grid>
                  <Grid item xs={12} margin='1rem'/>
                </Grid>
                <Box maxWidth='sm' sx={{display:'flex', justifyContent:'center', py:3, pb:5}}>
                  <Button variant='contained' endIcon={<ArrowForwardIosRoundedIcon />} href="/catalog/search" sx={sxbs} 
                  onClick={() => {props.fetchFlightsSearch(formData.departureAirport,formData.arrivalAirport,inputDate)}}>SEARCH FLIGHTS</Button>
                </Box>
                
              </Box>
          </Box>
          
      </Container>
    </div>
  )
}

export default FlightSearch