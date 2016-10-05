import React, { PropTypes } from 'react';
import Event from './Event';

const Events = ({ events }) => (
  <div className="row clearfix hero">
  {
    events.map((event) => {
      return <Event { ...event } />
    })
  }
  </div>
);

Events.propTypes = {
  events: PropTypes.arrayOf(PropTypes.shape(Event.propTypes))
};

export default Events;
