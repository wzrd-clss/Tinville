from designer_shop.views import *
from django.test import TestCase
import json

class DesignerShopTests(TestCase):
    fixtures = ['all.json',]

    #Item Variant Service Tests

    def test_nofiltersizeset(self):
        thecorrectresponse =json.loads('''{"variants": [{"color": "Red", "currency": "$", "sizeorder": 1, "price": "12.99", "quantity": 10, "size": "XXS"},
                                        {"color": "Blue", "currency": "$", "sizeorder": 1, "price": "12.99", "quantity": 10, "size": "XXS"},
                                        {"color": "Red", "currency": "$", "sizeorder": 2, "price": "12.99", "quantity": 10, "size": "XS"},
                                        {"color": "Blue", "currency": "$", "sizeorder": 2,"price": "12.99", "quantity": 10, "size": "XS"},
                                        {"color": "Red", "currency": "$", "sizeorder": 3, "price": "12.99", "quantity": 10, "size": "SM"},
                                        {"color": "Blue", "currency": "$", "sizeorder": 3, "price": "12.99", "quantity": 10, "size": "SM"}],
                                        "sizetype": "1", "minprice": "12.99"}''')
        self.checkfilter("TestSizeSetItem", None, thecorrectresponse)

    def test_pricefiltersizeset(self):
        thecorrectresponse = json.loads('''{"variants": {"12.99": [{"color": "Red", "currency": "$", "sizeorder": 1, "quantity": 10, "size": "XXS"},
                                           {"color": "Blue", "currency": "$", "sizeorder": 1, "quantity": 10, "size": "XXS"},
                                           {"color": "Red", "currency": "$", "sizeorder": 2, "quantity": 10, "size": "XS"},
                                           {"color": "Blue", "currency": "$", "sizeorder": 2, "quantity": 10, "size": "XS"},
                                           {"color": "Red", "currency": "$", "sizeorder": 3, "quantity": 10, "size": "SM"},
                                           {"color": "Blue", "currency": "$", "sizeorder": 3, "quantity": 10, "size": "SM"}]},
                                           "sizetype": "1", "minprice": "12.99"}''')
        self.checkfilter("TestSizeSetItem", "price", thecorrectresponse)

    def test_colorfiltersizeset(self):
        thecorrectresponse = json.loads('''{"variants": {"Blue": [{"currency": "$", "sizeorder": 1, "price": "12.99", "quantity": 10, "size": "XXS"},
                                           {"currency": "$", "sizeorder": 2, "price": "12.99", "quantity": 10, "size": "XS"},
                                           {"currency": "$", "sizeorder": 3, "price": "12.99", "quantity": 10, "size": "SM"}],
                                           "Red": [{"currency": "$", "sizeorder": 1, "price": "12.99", "quantity": 10, "size": "XXS"},
                                           {"currency": "$", "sizeorder": 2, "price": "12.99", "quantity": 10, "size": "XS"},
                                           {"currency": "$", "sizeorder": 3, "price": "12.99", "quantity": 10, "size": "SM"}]},
                                           "sizetype": "1", "minprice": "12.99"}''')
        self.checkfilter("TestSizeSetItem", "color", thecorrectresponse)

    def test_sizefiltersizeset(self):
        thecorrectresponse = json.loads('''{"variants": {"XXS": [{"color": "Blue", "currency": "$", "sizeorder": 1, "price": "12.99", "quantity": 10},
                                           {"color": "Red", "currency": "$", "sizeorder": 1, "price": "12.99", "quantity": 10}],
                                           "XS": [{"color": "Blue", "currency": "$", "sizeorder": 2, "price": "12.99", "quantity": 10},
                                           {"color": "Red", "currency": "$", "sizeorder": 2, "price": "12.99", "quantity": 10}],
                                           "SM": [{"color": "Blue", "currency": "$", "sizeorder": 3, "price": "12.99", "quantity": 10},
                                           {"color": "Red", "currency": "$", "sizeorder": 3, "price": "12.99", "quantity": 10}]},
                                           "sizetype": "1", "minprice": "12.99"}''')
        self.checkfilter("TestSizeSetItem", "size", thecorrectresponse)

    def test_quantityfiltersizeset(self):
        thecorrectresponse = json.loads('''{"variants": {"10": [{"color": "Red", "currency": "$", "sizeorder": 1, "price": "12.99", "size": "XXS"},
                                           {"color": "Blue", "currency": "$", "sizeorder": 1, "price": "12.99", "size": "XXS"},
                                           {"color": "Red", "currency": "$", "sizeorder": 2, "price": "12.99", "size": "XS"},
                                           {"color": "Blue", "currency": "$", "sizeorder": 2, "price": "12.99", "size": "XS"},
                                           {"color": "Red", "currency": "$", "sizeorder": 3,"price": "12.99", "size": "SM"},
                                           {"color": "Blue", "currency": "$", "sizeorder": 3, "price": "12.99", "size": "SM"}]},
                                           "sizetype": "1", "minprice": "12.99"}''')
        self.checkfilter("TestSizeSetItem", "quantity", thecorrectresponse)

    def test_currencyfiltersizeset(self):
        thecorrectresponse = json.loads('''{"variants": {"$": [{"color": "Red", "price": "12.99", "sizeorder": 1, "quantity": 10, "size": "XXS"},
                                           {"color": "Blue", "price": "12.99", "sizeorder": 1, "quantity": 10, "size": "XXS"},
                                           {"color": "Red", "price": "12.99", "sizeorder": 2, "quantity": 10, "size": "XS"},
                                           {"color": "Blue", "price": "12.99", "sizeorder": 2, "quantity": 10, "size": "XS"},
                                           {"color": "Red", "price": "12.99", "sizeorder": 3, "quantity": 10, "size": "SM"},
                                           {"color": "Blue", "price": "12.99", "sizeorder": 3, "quantity": 10, "size": "SM"}]},
                                           "sizetype": "1", "minprice": "12.99"}''')
        self.checkfilter("TestSizeSetItem", "currency", thecorrectresponse)

    def test_nofiltersizenum(self):
        thecorrectresponse =json.loads('''{"variants": [{"color": "Red", "currency": "$", "price": "12.99", "quantity": 10, "size": "1.0"},
                                          {"color": "Blue", "currency": "$", "price": "12.99", "quantity": 10, "size": "1.0"},
                                          {"color": "Red", "currency": "$", "price": "12.99", "quantity": 10, "size": "2.0"},
                                          {"color": "Blue", "currency": "$", "price": "12.99", "quantity": 10, "size": "2.0"},
                                          {"color": "Red", "currency": "$", "price": "12.99", "quantity": 10, "size": "3.0"},
                                          {"color": "Blue", "currency": "$", "price": "12.99", "quantity": 10, "size": "3.0"}],
                                          "sizetype": "3", "minprice": "12.99"}''')
        self.checkfilter("TestSizeNumberItem", None, thecorrectresponse)

    def test_pricefiltersizenum(self):
        thecorrectresponse = json.loads('''{"variants": {"12.99": [{"color": "Red", "currency": "$", "quantity": 10, "size": "1.0"},
                                           {"color": "Blue", "currency": "$", "quantity": 10, "size": "1.0"},
                                           {"color": "Red", "currency": "$", "quantity": 10, "size": "2.0"},
                                           {"color": "Blue", "currency": "$", "quantity": 10, "size": "2.0"},
                                           {"color": "Red", "currency": "$", "quantity": 10, "size": "3.0"},
                                           {"color": "Blue", "currency": "$", "quantity": 10, "size": "3.0"}]},
                                           "sizetype": "3", "minprice": "12.99"}''')
        self.checkfilter("TestSizeNumberItem", "price", thecorrectresponse)

    def test_colorfiltersizenum(self):
        thecorrectresponse = json.loads('''{"variants": {"Blue": [{"currency": "$", "price": "12.99", "quantity": 10, "size": "1.0"},
                                           {"currency": "$", "price": "12.99", "quantity": 10, "size": "2.0"},
                                           {"currency": "$", "price": "12.99", "quantity": 10, "size": "3.0"}],
                                           "Red": [{"currency": "$", "price": "12.99", "quantity": 10, "size": "1.0"},
                                           {"currency": "$", "price": "12.99", "quantity": 10, "size": "2.0"},
                                           {"currency": "$", "price": "12.99", "quantity": 10, "size": "3.0"}]},
                                           "sizetype": "3", "minprice": "12.99"}''')
        self.checkfilter("TestSizeNumberItem", "color", thecorrectresponse)

    def test_sizefiltersizenum(self):
        thecorrectresponse = json.loads('''{"variants": {"2.0": [{"color": "Blue", "currency": "$", "price": "12.99", "quantity": 10},
                                           {"color": "Red", "currency": "$", "price": "12.99", "quantity": 10}],
                                           "1.0": [{"color": "Blue", "currency": "$", "price": "12.99", "quantity": 10},
                                           {"color": "Red", "currency": "$", "price": "12.99", "quantity": 10}],
                                           "3.0": [{"color": "Blue", "currency": "$", "price": "12.99", "quantity": 10},
                                           {"color": "Red", "currency": "$", "price": "12.99", "quantity": 10}]},
                                           "sizetype": "3", "minprice": "12.99"}''')
        self.checkfilter("TestSizeNumberItem", "size", thecorrectresponse)

    def test_quantityfiltersizenum(self):
        thecorrectresponse = json.loads('''{"variants": {"10": [{"color": "Red", "currency": "$", "price": "12.99", "size": "1.0"},
                                           {"color": "Blue", "currency": "$", "price": "12.99", "size": "1.0"},
                                           {"color": "Red", "currency": "$", "price": "12.99", "size": "2.0"},
                                           {"color": "Blue", "currency": "$", "price": "12.99", "size": "2.0"},
                                           {"color": "Red", "currency": "$", "price": "12.99", "size": "3.0"},
                                           {"color": "Blue", "currency": "$", "price": "12.99", "size": "3.0"}]},
                                           "sizetype": "3", "minprice": "12.99"}''')
        self.checkfilter("TestSizeNumberItem", "quantity", thecorrectresponse)

    def test_currencyfiltersizenum(self):
        thecorrectresponse = json.loads('''{"variants": {"$": [{"color": "Red", "price": "12.99", "quantity": 10, "size": "1.0"},
                                           {"color": "Blue", "price": "12.99", "quantity": 10, "size": "1.0"},
                                           {"color": "Red", "price": "12.99", "quantity": 10, "size": "2.0"},
                                           {"color": "Blue", "price": "12.99", "quantity": 10, "size": "2.0"},
                                           {"color": "Red", "price": "12.99", "quantity": 10, "size": "3.0"},
                                           {"color": "Blue", "price": "12.99", "quantity": 10, "size": "3.0"}]},
                                           "sizetype": "3", "minprice": "12.99"}''')
        self.checkfilter("TestSizeNumberItem", "currency", thecorrectresponse)

    def test_nofiltersizedim(self):
        thecorrectresponse =json.loads('''{"variants": [{"color": "Red", "currency": "$", "price": "12.99", "quantity": 10, "size": "30.0 x 30.0"},
                                          {"color": "Blue", "currency": "$", "price": "12.99", "quantity": 10, "size": "31.0 x 31.0"},
                                          {"color": "Red", "currency": "$", "price": "12.99", "quantity": 10, "size": "32.0 x 32.0"},
                                          {"color": "Blue", "currency": "$", "price": "12.99", "quantity": 10, "size": "30.0 x 30.0"},
                                          {"color": "Red", "currency": "$", "price": "12.99", "quantity": 10, "size": "31.0 x 31.0"},
                                          {"color": "Blue", "currency": "$", "price": "12.99", "quantity": 10, "size": "32.0 x 32.0"}],
                                          "sizetype": "2", "minprice": "12.99"}''')
        self.checkfilter("TestSizeDimensionItem", None, thecorrectresponse)

    def test_pricefiltersizedim(self):
        thecorrectresponse = json.loads('''{"variants": {"12.99": [{"color": "Red", "currency": "$", "quantity": 10, "size": "30.0 x 30.0"},
                                           {"color": "Blue", "currency": "$", "quantity": 10, "size": "31.0 x 31.0"},
                                           {"color": "Red", "currency": "$", "quantity": 10, "size": "32.0 x 32.0"},
                                           {"color": "Blue", "currency": "$", "quantity": 10, "size": "30.0 x 30.0"},
                                           {"color": "Red", "currency": "$", "quantity": 10, "size": "31.0 x 31.0"},
                                           {"color": "Blue", "currency": "$", "quantity": 10, "size": "32.0 x 32.0"}]},
                                           "sizetype": "2", "minprice": "12.99"}''')
        self.checkfilter("TestSizeDimensionItem", "price", thecorrectresponse)

    def test_colorfiltersizedim(self):
        thecorrectresponse = json.loads('''{"variants": {"Blue": [{"currency": "$", "price": "12.99", "quantity": 10, "size": "30.0 x 30.0"},
                                           {"currency": "$", "price": "12.99", "quantity": 10, "size": "31.0 x 31.0"},
                                           {"currency": "$", "price": "12.99", "quantity": 10, "size": "32.0 x 32.0"}],
                                           "Red": [{"currency": "$", "price": "12.99", "quantity": 10, "size": "30.0 x 30.0"},
                                           {"currency": "$", "price": "12.99", "quantity": 10, "size": "31.0 x 31.0"},
                                           {"currency": "$", "price": "12.99", "quantity": 10, "size": "32.0 x 32.0"}]},
                                           "sizetype": "2", "minprice": "12.99"}''')
        self.checkfilter("TestSizeDimensionItem", "color", thecorrectresponse)

    def test_sizefiltersizedim(self):
        thecorrectresponse = json.loads('''{"variants": {"32.0 x 32.0": [{"color": "Blue", "currency": "$", "price": "12.99", "quantity": 10},
                                           {"color": "Red", "currency": "$", "price": "12.99", "quantity": 10}],
                                           "31.0 x 31.0": [{"color": "Blue", "currency": "$", "price": "12.99", "quantity": 10},
                                           {"color": "Red", "currency": "$", "price": "12.99", "quantity": 10}],
                                           "30.0 x 30.0": [{"color": "Blue", "currency": "$", "price": "12.99", "quantity": 10},
                                           {"color": "Red", "currency": "$", "price": "12.99", "quantity": 10}]},
                                           "sizetype": "2", "minprice": "12.99"}''')
        self.checkfilter("TestSizeDimensionItem", "size", thecorrectresponse)

    def test_quantityfiltersizedim(self):
        thecorrectresponse = json.loads('''{"variants": {"10": [{"color": "Red", "currency": "$", "price": "12.99", "size": "30.0 x 30.0"},
                                           {"color": "Blue", "currency": "$", "price": "12.99", "size": "31.0 x 31.0"},
                                           {"color": "Red", "currency": "$", "price": "12.99", "size": "32.0 x 32.0"},
                                           {"color": "Blue", "currency": "$", "price": "12.99", "size": "30.0 x 30.0"},
                                           {"color": "Red", "currency": "$", "price": "12.99", "size": "31.0 x 31.0"},
                                           {"color": "Blue", "currency": "$", "price": "12.99", "size": "32.0 x 32.0"}]},
                                           "sizetype": "2", "minprice": "12.99"}''')
        self.checkfilter("TestSizeDimensionItem", "quantity", thecorrectresponse)

    def test_currencyfiltersizedim(self):
        thecorrectresponse = json.loads('''{"variants": {"$": [{"color": "Red", "price": "12.99", "quantity": 10, "size": "30.0 x 30.0"},
                                           {"color": "Blue", "price": "12.99", "quantity": 10, "size": "31.0 x 31.0"},
                                           {"color": "Red", "price": "12.99", "quantity": 10, "size": "32.0 x 32.0"},
                                           {"color": "Blue", "price": "12.99", "quantity": 10, "size": "30.0 x 30.0"},
                                           {"color": "Red", "price": "12.99", "quantity": 10, "size": "31.0 x 31.0"},
                                           {"color": "Blue", "price": "12.99", "quantity": 10, "size": "32.0 x 32.0"}]},
                                           "sizetype": "2", "minprice": "12.99"}''')
        self.checkfilter("TestSizeDimensionItem", "currency", thecorrectresponse)

    def checkfilter(self, itemname, filtergroup, correctresponse):
        item = get_object_or_404(Product, slug__iexact=itemname, shop_id=1, parent__isnull=True)
        mybaseresponse = json.loads(get_variants(item, filtergroup))
        self.assertEqual(mybaseresponse, correctresponse, "the response was not as expected" )


    # Escaped Javascript tests
    def test_escaped_javascript_in_shop_about_editor(self):
        bad_script = "<script>alert('PWND!')</script>"
        self.client.login(username='demo@user.com', password='tinville')
        response = self.client.post('/demo/edit/', {'aboutBoxForm': 'Submit', 'aboutContent': bad_script})
        self.assertNotContains(response, bad_script)
        response = self.client.get('/demo/')
        self.assertNotContains(response, bad_script)

    def test_escaped_javascript_in_shop_item_editor(self):
        bad_script = "<script>alert('PWND!')</script>"
        with open('designer_shop/fixtures/media/image_not_found.jpg') as fp:
            self.client.login(username='demo@user.com', password='tinville')
            response = self.client.post('/demo/edit/',
                                        {'category': '37',
                                         'description': bad_script,
                                         'price': '3.00',
                                         'images-INITIAL_FORMS': '0',
                                         'images-MAX_NUM_FORMS': '5',
                                         'images-MIN_NUM_FORMS': '1',
                                         'images-TOTAL_FORMS': '1',
                                         'images-0-original': fp,
                                         'images-0-cropping': '',
                                         'sizeSetSelectionTemplate0_pc_colorSelection0': '8',
                                         'sizeSetSelectionTemplate0_pc_colorSelection1': '',
                                         'sizeSetSelectionTemplate0_quantityField0': '1',
                                         'sizeSetSelectionTemplate0_quantityField1': '1',
                                         'sizeSetSelectionTemplate0_sizeSetSelection': '2',
                                         'sizeSetSelectionTemplate1_sizeSetSelection': '',
                                         'sizeVariation': '1',
                                         'title': 'TestTitle'
                                        })
        self.assertNotContains(response, bad_script)
        response = self.client.get('/demo/testtitle/')
        self.assertNotContains(response, bad_script)

    def test_exception_on_missing_size_variation_info(self):
        self.client.login(username='demo@user.com', password='tinville')
        initial_products = len(Product.objects.all())
        with open('designer_shop/fixtures/media/image_not_found.jpg') as fp:
            response = self.client.post('/demo/edit/',
                                    {
                                     'category': '37',
                                     'description': 'Test Description',
                                     'price': '3.00',
                                     'images-INITIAL_FORMS': '0',
                                     'images-MAX_NUM_FORMS': '5',
                                     'images-MIN_NUM_FORMS': '1',
                                     'images-TOTAL_FORMS': '1',
                                     'images-0-original': fp,
                                     'images-0-cropping': '',
                                     'sizeSetSelectionTemplate0_pc_colorSelection0': '8',
                                     'sizeSetSelectionTemplate0_pc_colorSelection1': '',
                                     'sizeSetSelectionTemplate0_quantityField0': '1',
                                     'sizeSetSelectionTemplate0_quantityField1': '1',
                                     'sizeSetSelectionTemplate0_sizeSetSelection': '2',
                                     'sizeSetSelectionTemplate1_sizeSetSelection': '',
                                     'title': 'TestTitle'
                                    })

        self.assertEquals(len(Product.objects.all()), initial_products)  # No new products should have been made
        self.assertEquals(response.status_code, 400)

    def test_exception_on_missing_sizes(self):
        self.client.login(username='demo@user.com', password='tinville')
        initial_products = len(Product.objects.all())
        with open('designer_shop/fixtures/media/image_not_found.jpg') as fp:
            response = self.client.post('/demo/edit/',
                                    {
                                     'category': '37',
                                     'description': 'Test Description',
                                     'price': '3.00',
                                     'images-INITIAL_FORMS': '0',
                                     'images-MAX_NUM_FORMS': '5',
                                     'images-MIN_NUM_FORMS': '1',
                                     'images-TOTAL_FORMS': '1',
                                     'images-0-original': fp,
                                     'images-0-cropping': '',
                                     'sizeVariation': '1',
                                     'title': 'TestTitle'
                                    })
        self.assertEquals(len(Product.objects.all()), initial_products)  # No new products should have been made
        self.assertEquals(response.status_code, 400)


    def test_exception_on_missing_color(self):
        self.client.login(username='demo@user.com', password='tinville')
        initial_products = len(Product.objects.all())

        with open('designer_shop/fixtures/media/image_not_found.jpg') as fp:
            response = self.client.post('/demo/edit/',
                                    {
                                     'category': '37',
                                     'description': 'Test Description',
                                     'price': '3.00',
                                     'images-INITIAL_FORMS': '0',
                                     'images-MAX_NUM_FORMS': '5',
                                     'images-MIN_NUM_FORMS': '1',
                                     'images-TOTAL_FORMS': '1',
                                     'images-0-original': fp,
                                     'images-0-cropping': '',
                                     'sizeSetSelectionTemplate0_quantityField0': '1',
                                     'sizeSetSelectionTemplate0_quantityField1': '1',
                                     'sizeSetSelectionTemplate0_sizeSetSelection': '2',
                                     'sizeSetSelectionTemplate1_sizeSetSelection': '',
                                     'sizeVariation': '1',
                                     'title': 'TestTitle'
                                    })
        self.assertEquals(len(Product.objects.all()), initial_products)  # No new products should have been made
        self.assertEquals(response.status_code, 400)


    def test_exception_on_missing_quantities(self):
        self.client.login(username='demo@user.com', password='tinville')
        initial_products = len(Product.objects.all())
        with open('designer_shop/fixtures/media/image_not_found.jpg') as fp:
            response = self.client.post('/demo/edit/',
                                    {
                                     'category': '37',
                                     'description': 'Test Description',
                                     'price': '3.00',
                                     'images-INITIAL_FORMS': '0',
                                     'images-MAX_NUM_FORMS': '5',
                                     'images-MIN_NUM_FORMS': '1',
                                     'images-TOTAL_FORMS': '1',
                                     'images-0-original': fp,
                                     'images-0-cropping': '',
                                     'sizeSetSelectionTemplate0_pc_colorSelection0': '8',
                                     'sizeSetSelectionTemplate0_pc_colorSelection1': '',
                                     'sizeSetSelectionTemplate0_sizeSetSelection': '2',
                                     'sizeSetSelectionTemplate1_sizeSetSelection': '',
                                     'sizeVariation': '1',
                                     'title': 'TestTitle'
                                    })
        self.assertEquals(len(Product.objects.all()), initial_products)  # No new products should have been made
        self.assertEquals(response.status_code, 400)

    def test_exception_on_negative_quantities(self):
        self.client.login(username='demo@user.com', password='tinville')
        initial_products = len(Product.objects.all())
        with open('designer_shop/fixtures/media/image_not_found.jpg') as fp:
            response = self.client.post('/demo/edit/',
                                    {
                                     'category': '37',
                                     'description': 'Test Description',
                                     'price': '3.00',
                                     'images-INITIAL_FORMS': '0',
                                     'images-MAX_NUM_FORMS': '5',
                                     'images-MIN_NUM_FORMS': '1',
                                     'images-TOTAL_FORMS': '1',
                                     'images-0-original': fp,
                                     'images-0-cropping': '',
                                     'sizeSetSelectionTemplate0_quantityField0': '-1',
                                     'sizeSetSelectionTemplate0_quantityField1': '1',
                                     'sizeSetSelectionTemplate0_pc_colorSelection0': '8',
                                     'sizeSetSelectionTemplate0_pc_colorSelection1': '',
                                     'sizeSetSelectionTemplate0_sizeSetSelection': '2',
                                     'sizeSetSelectionTemplate1_sizeSetSelection': '',
                                     'sizeVariation': '1',
                                     'title': 'TestTitle'
                                    })
        self.assertEquals(len(Product.objects.all()), initial_products)  # No new products should have been made


    def test_exception_on_negative_price(self):
        self.client.login(username='demo@user.com', password='tinville')
        initial_products = len(Product.objects.all())
        with open('designer_shop/fixtures/media/image_not_found.jpg') as fp:
            response = self.client.post('/demo/edit/',
                                    {
                                     'category': '37',
                                     'description': 'Test Description',
                                     'price': '-3.00',
                                     'images-INITIAL_FORMS': '0',
                                     'images-MAX_NUM_FORMS': '5',
                                     'images-MIN_NUM_FORMS': '1',
                                     'images-TOTAL_FORMS': '1',
                                     'images-0-original': fp,
                                     'images-0-cropping': '',
                                     'sizeSetSelectionTemplate0_quantityField0': '1',
                                     'sizeSetSelectionTemplate0_quantityField1': '1',
                                     'sizeSetSelectionTemplate0_pc_colorSelection0': '8',
                                     'sizeSetSelectionTemplate0_pc_colorSelection1': '',
                                     'sizeSetSelectionTemplate0_sizeSetSelection': '2',
                                     'sizeSetSelectionTemplate1_sizeSetSelection': '',
                                     'sizeVariation': '1',
                                     'title': 'TestTitle'
                                    })
        self.assertEquals(len(Product.objects.all()), initial_products)  # No new products should have been made
