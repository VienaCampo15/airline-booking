import React from 'react'
import { Card, CardContent, Divider, Grid, Stack, Typography } from '@mui/material'
import FlightTakeoffIcon from '@mui/icons-material/FlightTakeoff';
import FlightLandIcon from '@mui/icons-material/FlightLand';
import AccessTimeFilledOutlinedIcon from '@mui/icons-material/AccessTimeFilledOutlined';

const SearchCard = (props) => {
  const sxcard = {'my':2, 'mx':6, 'height':180,
                  'bgcolor':'#c19ee0', 'boxShadow':3,
                  'borderBottom':4, 'borderBottomColor':'#240046',
                  'backgroundImage':'linear-gradient(90deg, #d2b7e5, #b185db, #d2b7e5)',
                  'backgroundSize':'250%', 'transition':'0.5s',
                  '&:hover': {'bgcolor':'#3C096C', 'backgroundPosition':'right'} };
  return (
    <div>
        <Card sx={sxcard}>
            <CardContent>
                    <Grid container rowSpacing={1}>
                      <Grid item xs={2}>
                        <Typography sx={{fontWeight:'bold', fontSize:13, textAlign:'center', color:'#5A189A'}}>
                            DEPARTURE
                        </Typography>
                        <Typography sx={{fontWeight:'900', fontSize:23, textAlign:'center', color:'#240046'}}>
                            {props.departureAirportTime}
                        </Typography>
                      </Grid>

                      <Grid item flexGrow={1}/>

                      <Grid item xs={2}>
                        <Typography sx={{fontWeight:'bold', fontSize:13, textAlign:'center', color:'#5A189A'}}>
                            ARRIVAL
                        </Typography>
                        <Typography sx={{fontWeight:'900', fontSize:23, textAlign:'center', color:'#240046'}}>
                            {props.arrivalAirportTime}
                        </Typography>
                      </Grid>

                      <Grid item xs={12}> <Divider variant="middle" /> </Grid>

                      <Grid item xs={1}>
                        <FlightTakeoffIcon fontSize='large'/>
                      </Grid>
                      <Grid item xs={1} sx={{display:'flex', justifyContent:'center', alignItems:'center'}}>
                        <Typography sx={{fontWeight:'bold', fontSize:15, color:'#5A189A'}}>
                            {props.departureAirportCode}
                        </Typography>
                      </Grid>
                      
                      <Grid item flexGrow={1} sx={{display:'flex', justifyContent:'center'}}>
                        <Stack direction="row" maxWidth={100} sx={{bgcolor: '#240046', boxShadow:1, borderRadius:1, px:0.5, alignItems:'center'}}>
                            <AccessTimeFilledOutlinedIcon fontSize='large' sx={{color:'#E0AAFF'}}/>
                            <Typography sx={{fontWeight:'bold', fontSize:15, color:'#E0AAFF', ml:0.5}}>
                                {props.flightTime}
                            </Typography>
                        </Stack>
                      </Grid>

                      <Grid item xs={1}>
                        <FlightLandIcon fontSize='large'/>
                      </Grid>
                      <Grid item xs={1} sx={{display:'flex', justifyContent:'center', alignItems:'center'}}>
                        <Typography sx={{fontWeight:'bold', fontSize:15, textAlign:'center', color:'#5A189A'}}>
                            {props.arrivalAirportCode}
                        </Typography>
                      </Grid>

                      <Grid item xs={12}> <Divider variant="middle" /> </Grid>

                      <Grid item xs={3}>
                        <Typography sx={{fontWeight:'bold', fontSize:14, textAlign:'center', color:'#5A189A'}}>
                            {props.ticketCurrency} {props.ticketPrice}
                        </Typography>
                      </Grid>

                      <Grid item flexGrow={1}/>

                      <Grid item xs={2}>
                        <Typography sx={{fontWeight:'bold', fontSize:14, textAlign:"center", color:'#5A189A'}}>
                            Flight {props.flightNumber}
                        </Typography>
                      </Grid>
                    </Grid>
                
            </CardContent>
        </Card>
    </div>
  )
}

export default SearchCard