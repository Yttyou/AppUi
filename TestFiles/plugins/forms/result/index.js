// 读取覆盖、通过率 json
var model2JSON;
var url = "data/rate_data.json";
var request = new XMLHttpRequest();
request.open("get", url);
request.send(null);
request.onload = function () {
    model2JSON = JSON.parse(request.responseText);
}

var SP_BP_resultsFormModel = Backbone.Collection.extend({
    url: 'data/SP_BP_results.json'
})

class Passed extends allure.components.AppLayout {

    initialize() {
        this.model = new SP_BP_resultsFormModel();
    }

    loadData() {
        return this.model.fetch();
    }

    getContentView() {
        return new PassedView({ items: this.model.models, items2: model2JSON });
    }
}

const passed_template = function (data) {
    html = `<div class="pane__title pane__title_borderless"><span class="pane__title-text">通过率</span></div>`
    // 通过率 html
    html += `<div style="overflow-y: scroll;max-height: 50vh;">
            <table class="attachment__table" id="form"><thead><tr>
            <th>模块</th>
            <th>通过率</th>
            </tr></thead>`;    
    html += `<tbody>`;
    for (var item2 of data.items2) {
        html += `<tr>
                <td>${item2['Module']}</td>
                <td>${(item2['Passed Rate'] * 100).toFixed(2)}%</td>`
    }
    html += `</tbody></table></div>`;
    // 通过模块 html
    html += `<div class="pane__title pane__title_borderless" style="margin-top: 20px;"><span class="pane__title-text">通过模块</span></div>`
    html += `<div style="overflow-y: scroll;height: 100vh;">
            <table class="attachment__table" id="form"><thead><tr>
            <th>一级模块</th>
            <th>二级模块</th>
            <th>三级模块</th>
            <th>四级模块</th>
            <th>五级模块</th>
            <th>测试是否通过</th>
            </tr></thead>`;
    html += `<tbody>`;
    for (var item of data.items) {
        if (item.attributes['Covered'] == '') {
            continue;
        }
        html += `<tr>
                <td>${item.attributes['1']}</td>
                <td>${item.attributes['2']}</td>
                <td>${item.attributes['3']}</td>
                <td>${item.attributes['4']}</td>
                <td>${item.attributes['5']}</td>
                <td>${item.attributes['Results']}</td>
                </tr>`;
    }
    html += `</tbody></table></div>`;
    return html;
}
//在allure报告的左边增加一个tab按钮
var PassedView = Backbone.Marionette.View.extend({
    template: passed_template,

    render: function () {
        this.$el.html(this.template(this.options));
        return this;
    }
})

//
allure.api.addTab('passed', {
    title: 'tab.passed.name', icon: 'fa fa-table',
    route: 'passed',
    onEnter: (function () {
        return new Passed()
    })
});

// wiget中展示
class PassedWidget extends Backbone.Marionette.View {

    template(data) {
        return widgetTemplate(data)
    }

    serializeData() {
        return {
            items: this.model.get('items'),
        }
    }
}

allure.api.addWidget('passed_widget', PassedWidget);

// 多语言支持。使用位置：allure.api.addTab() 中的 title 项
allure.api.addTranslation('zh', {
    tab: {
        passed: {
            name: '通过率'
        }
    }
});
allure.api.addTranslation('zt', {
    tab: {
        passed: {
            name: '通過率'
        }
    }
});

allure.api.addTranslation('en', {
    tab: {
        passed: {
            name: 'Passed Rate'
        }
    }
});