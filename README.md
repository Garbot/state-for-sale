# Researching Money in Politics in North Carolina

I initially decided to begin researching this topic while watching the World Series.  I felt
disgust while watching an expensive ad from a vaguely-named super PAC
attack a relatively minor state-level politician (*which?  Go back and check*).  The amount of resources poured into these races is
staggering, and it's difficult for the average citizen to keep up with.

The North Carolina [State Board Of Elections](http://cf.ncsbe.gov/cf_rpt_search_type/) makes this data public, but it is somewhat difficult to parse.  Data is available in many cases in the form of scanned images of required disclosure forms, but there is in many cases no way to obtain this data in a machine-readable, electronic format.  Luckily, the [Institute For Southern Studies](http://followncmoney.org/expenditures/all) has done great work in going through these items and converting them to electronic format.  However, I have had trouble locating data in a machine-readable format such as JSON.

### Helpful links
* http://www.wral.com/tracking-who-gives-what-to-nc-lawmakers/14586531/
* [WRAL overview of state level campaign finance](http://www.wral.com/how-money-flows-into-elections-/13393371/)
* https://github.com/wraldata/donor-reveal/blob/master/donor_reveal.js
* [WRAL's JSON file of NC Legislature Members](http://www.wral.com/news/state/nccapitol/data_set/14376504/?dsi_id=ncga-eid&version=jsonObj)
* [Sunlight Foundation overview of federal campaign finance](http://realtime.influenceexplorer.com/about/#form_types)

### Possible data sources
* http://www.followthemoney.org/our-data/apis/support/
* http://cf.ncsbe.gov/cf_rpt_search_type/
* http://followncmoney.org/expenditures/all
* https://api.open.fec.gov/developers/#!/committee/get_candidate_candidate_id_committees
* https://www.opensecrets.org/outsidespending/summ.php?disp=R
* http://sunlightlabs.github.io/realtime-docs/
* [example JSON from the above for a single disclosure](http://realtime.influenceexplorer.com/api/new_filing/?filing_number=1116653&format=json&apikey=54a6b8a30ac049e887ddef7df9fdaba0)

### Presentation
The plan is to take this data and make a website that presents it in a more user-friendly, navigable form, perhaps using a d3.js map.
* https://maptimeboston.github.io/d3-maptime/#/
* http://jsonprettyprint.com/
* https://bost.ocks.org/mike/map/
* http://bl.ocks.org/mbostock/4060606

* https://github.com/maptimeBoston/d3-maptime
^^ error with loading HTTP over HTTPS on the boston maps - pull and fix :)
