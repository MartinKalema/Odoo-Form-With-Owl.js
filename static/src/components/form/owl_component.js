/* @odoo-module */

import { Component, mount, whenReady, xml } from '@odoo/owl'
import { templates } from "@web/core/assets"

// Header component
class PageHeader extends Component {
    static template = "nira_data_entry.header"
}

// Card component
class FormCard extends Component {
    static template = "nira_data_entry.card"

    setup(){
        this.date = new Date().toLocaleString()
    }
}

// Parent component
class DataEntryFormComponent extends Component{
    setup(){
    }
}

DataEntryFormComponent.template = 'nira_data_entry.parent'
// Declare components
DataEntryFormComponent.components = { PageHeader, FormCard }


whenReady(()=>{
    const element_with_class_name = document.querySelector('.owl_template')
//    if an element with that class name exists
    if(element_with_class_name){
        mount(DataEntryFormComponent, element_with_class_name, { templates })
    }
})