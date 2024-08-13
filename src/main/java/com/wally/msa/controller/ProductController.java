package com.wally.msa.controller;

import com.wally.msa.controller.dto.ProductRequest;
import com.wally.msa.controller.dto.ProductResponse;
import com.wally.msa.product.model.Product;
import com.wally.msa.service.ProductService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/products")
@RequiredArgsConstructor
public class ProductController {

    private final ProductService productService;

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public ProductResponse createProduct(
            @RequestBody ProductRequest productRequest) {

        return productService.createProduct(productRequest);
    }

    @GetMapping
    @ResponseStatus(HttpStatus.OK)
    public List<ProductResponse> getProducts() {

        return productService.getProducts();
    }
}
