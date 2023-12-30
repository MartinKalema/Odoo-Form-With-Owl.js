/* @odoo-module */

import { Component, mount, whenReady, xml } from '@odoo/owl'
import { templates } from "@web/core/assets"

class DataEntryFormComponent extends Component{

}

DataEntryFormComponent.template = 'nira_data_entry.owl_js_template'

//DataEntryFormComponent.template = xml`<div>Hurray, Problem solved</div>`

whenReady(()=>{
    const element_with_class_name = document.querySelector('.owl_template')
//    if an element with that class name exists
    if(element_with_class_name){
        mount(DataEntryFormComponent, element_with_class_name, { templates })
    }
})